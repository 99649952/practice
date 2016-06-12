from django.contrib import admin

from app01 import models
# admin.site.register(models.Author)
# admin.site.register(models.Book)
# admin.site.register(models.Publisher)
admin.site.register(models.HostGroup)
admin.site.register(models.Host)
admin.site.register(models.User_Login)