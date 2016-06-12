#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
from myauth import UserProfile
from rest_framework import serializers


#restfull页面显示内容
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'name', 'email', 'is_admin')
