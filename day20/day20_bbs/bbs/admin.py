from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.User_Login)
admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserGroup)
admin.site.register(models.UserInfo)
