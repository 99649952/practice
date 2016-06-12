from django.db import models

# Create your models here.
class Assets(models.Model):
    serial_number = models.CharField(max_length=20)
    business_ip = models.CharField(max_length=15)
    manage_ip = models.CharField(max_length=15)
    status = models.CharField(max_length=5)