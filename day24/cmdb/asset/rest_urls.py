#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
from django.conf.urls import url, include
from rest_framework import routers
import rest_views as views

#将restfull相关链接注册

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.urls)),
]