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
