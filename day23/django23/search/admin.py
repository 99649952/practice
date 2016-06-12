from django.contrib import admin
import models

admin.site.register(models.HostGroup)
admin.site.register(models.Host)
admin.site.register(models.HostGroupRelevance)