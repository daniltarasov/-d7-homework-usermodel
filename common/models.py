from django.db import models
from django.contrib.auth.models import User  
from allauth.socialaccount.models import SocialAccount
# from SocialAccount.fields import JSONField
# import json
# Create your models here.

  
  
class UserProfile(models.Model):  
  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)

# class SocialAccauntProfile(SocialAccount):
class SocialAccauntProfile(models.Model):
    age = models.IntegerField()  
    user = models.OneToOneField(SocialAccount, on_delete=models.CASCADE, related_name='profile', blank=True)
    extra_data_profile = models.TextField(blank=True)
    # extra_data_profile = JSONField(verbose_name=_('extra data'), default=dict)
    # name = models.CharField(max_length=50, default="Ваня", null=False)
    name = models.CharField(max_length=50)
    # country = models.CharField(max_length=20, default=None, blank=True, null=True)
    # country = models.CharField(max_length=20, default="Россия", null=False)
    city = models.CharField(max_length=20)

# class SocialAccauntProfile(SocialAccount):
#     age = models.IntegerField()  
#     user = models.OneToOneField(SocialAccount, on_delete=models.CASCADE, related_name='profile', blank=True)


