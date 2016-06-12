#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
import myauth
from rest_framework import viewsets
from serializers import UserSerializer


#数据库中提取数据关联到restfull视图中

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = myauth.UserProfile.objects.all()
    serializer_class = UserSerializer


