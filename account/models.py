from django.db import models
from django.contrib.auth.models import User


from django_countries.fields import CountryField
from localflavor.us.models import USStateField, USZipCodeField
# Create your models here.
class UserProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    country = CountryField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    postal_code = USZipCodeField(blank=True, null=True)

    def get_absolute_url(self):
        return self.profile_pic.url

    def __str__(self):
        return self.username
