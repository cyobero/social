from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    profile_pic = models.ImageField(upload_to='/profile_pics', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
