from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


from django_countries.fields import CountryField
from localflavor.us.models import USStateField, USZipCodeField
from blurb.models import Blurb
from friendship.models import Friend
from birthday.fields import BirthdayField
# Create your models here.


class UserProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('C', 'Cheeseburger'),
    )
    profile_pic = models.ImageField(upload_to='profile_pics/',
                                    default='default_profile.png', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birthday = BirthdayField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    postal_code = USZipCodeField(blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return self.profile_pic.url

    def get_blurbs(self):
        return Blurb.objects.filter(author=self)

    def __str__(self):
        return self.username

    def get_friends_profiles(self):
        """Returns a list of friends' user profiles."""
        friends = Friend.objects.friends(self)
        profiles = [get_object_or_404(UserProfile, username=friend.username) for friend in
                    friends]
        return profiles
