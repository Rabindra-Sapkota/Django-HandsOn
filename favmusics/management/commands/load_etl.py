from django.core.management import BaseCommand
from favmusics.models import ParsedClaim, Payer, ClaimLine, ServiceLine, JobHistory
from typing import Any
# from django.contrib.postgres.aggregates import ArrayAgg
from django.db import transaction


def get_payer(edi_payer_id, client_partition_id, payer_name=None):
    payers = Payer.objects.filter(edi_payer_id=edi_payer_id).first()
    return payers

class Command(BaseCommand):
    help = "Loads data from sample_data.csv into database"

    def handle(self, *args: Any, **options: Any) -> None:
        if JobHistory.objects.exclude(status='COMPLETED').filter(name__in=('DeltaLoad', 'DeltaExtract')).count():
            raise Exception ("JOB still running")

        LoadJob = JobHistory.objects.create(name='DeltaLoad')
        # (started time, status is default)

        # for parsed_claim in ParsedClaim.objects.values('claim_number', 'client_partition', 'claim_amount', 'edi_payer_id').annotate(cpt_code=ArrayAgg('cpt_code')):
        for parsed_claim in ParsedClaim.objects.values('claim_number', 'client_partition', 'claim_amount', 'edi_payer_id').distinct():
            try:
                edi_payer_id = parsed_claim.pop('edi_payer_id')
                payer = get_payer(edi_payer_id, 'te')
                parsed_claim['payer_id'] = payer
                with transaction.atomic():
                    claim_line = ClaimLine.objects.create(**parsed_claim)
                    for service_line in ParsedClaim.objects.filter(claim_number=parsed_claim['claim_number']).values('service_line'):
                        service_line['claims_line_id'] = claim_line
                        ServiceLine.objects.create(**service_line)
                    parsed_claim.status = 'Loaded'
                    parsed_claim.save()
            except Exception as e:
                parsed_claim.status = 'Failed'
                parsed_claim.status_message = str(e)
                parsed_claim.save()
        
        success_count = ParsedClaim.objects.filter(status='SUCCESS').count()
        failed_count = ParsedClaim.objects.filter(status='FAILED').count()
        LoadJob.success_count = success_count
        LoadJob.failed_count = failed_count
        LoadJob.completed_time = '2023-09-10 11:30:45'
        if success_count + failed_count != ParsedClaim.objects.count():
            LoadJob.satus = 'FailedToReconcile'
            LoadJob.save()
        LoadJob.satus = 'SUCCESS'
        LoadJob.save()
