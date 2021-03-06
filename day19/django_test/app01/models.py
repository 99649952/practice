from __future__ import unicode_literals
from django.db import models

# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()
#     def __unicode__(self):
#         return self.name
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     def __unicode__(self):
#         return u'%s %s' % (self.first_name, self.last_name)
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()
#     def __unicode__(self):
#         return self.title

class User_Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class HostGroup(models.Model):
    host_group_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.host_group_name
class Host(models.Model):
    host_group = models.ManyToManyField(HostGroup)
    hostname = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    def __unicode__(self):
        return self.hostname
