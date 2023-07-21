from django.db import models

class Customer(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=30)
    dob = models.DateField(null=True, verbose_name="Date Of Birth")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(blank=True)
    music = models.ManyToManyField("Music", blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True)


    def __str__(self) -> str:
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField()


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Musician'

class JobHistory(models.Model):
    pass

class ParsedClaim(models.Model):
    claim_number = models.CharField(max_length=50)
    claim_amount = models.FloatField()
    cpt_code = models.CharField(max_length=30)
    client_partition = models.CharField(max_length=50)
    edi_payer_id = models.CharField(max_length=30)
    service_line = models.CharField(max_length=30)


class Payer(models.Model):
    edi_payer_id = models.CharField(max_length=30)

    def __str__(self):
        return self.edi_payer_id

class ClaimLine(models.Model):
    claim_number = models.CharField(max_length=50)
    claim_amount = models.FloatField()
    cpt_code = models.CharField(max_length=30)
    client_partition = models.CharField(max_length=50)
    payer_id = models.ForeignKey(Payer, on_delete=models.RESTRICT)

    def __str__(self):
        return self.claim_number

    class Meta:
        unique_together = ['claim_number', 'client_partition']

class ServiceLine(models.Model):
    claims_line_id = models.ForeignKey(ClaimLine, on_delete=models.RESTRICT)
    service_line = models.CharField(max_length=30)
