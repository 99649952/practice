#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
from django import forms
import os

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'user','name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','name':'password'}))

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    category = forms.IntegerField()
    head_img = forms.ImageField(required=False)
    content = forms.CharField(min_length=10)

def handle_uploaded_file(request,f):
    base_img_upload_path = 'statics/imgs'
    user_path = "%s/%s" %(base_img_upload_path,request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open("%s/%s" %(user_path,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return  "/static/imgs/%s/%s" %(request.user.userprofile.id,f.name)