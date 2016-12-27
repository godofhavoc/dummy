from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    user_location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.user.first_name:
            if self.user.last_name:
                return self.user.first_name + ' ' + self.user.last_name
            else:
                return self.user.first_name
        else:
            return "No name"
