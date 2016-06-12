from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=50)
    privilege = models.CharField(max_length=32, default='user')
    status = models.CharField(max_length=32, default='start')
