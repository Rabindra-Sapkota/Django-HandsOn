from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Customer, Music, Payer, ParsedClaim, ClaimLine, ServiceLine

@admin.register(ClaimLine)
class ClaimLineAdmin(admin.ModelAdmin):
    list_display = ['claim_number', 'claim_amount', 'cpt_code', 'client_partition', 'payer_id']

@admin.register(ServiceLine)
class ServiceLineAdmin(admin.ModelAdmin):
    list_display = ['claims_line_id', 'service_line']

@admin.register(Payer)
class PayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'edi_payer_id']


@admin.register(ParsedClaim)
class ParsedClaimAdmin(admin.ModelAdmin):
    list_display = ['claim_number', 'claim_amount', 'cpt_code', 'client_partition', 'edi_payer_id', 'service_line']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'gender', 'id']
    list_filter = ['gender', 'dob']
    search_fields = ('name__startswith', 'gender')


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass

    def has_delete_permission(self, request, obj = None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
