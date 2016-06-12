#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
from django.shortcuts import render,redirect
from django import forms
import models
from django.core.exceptions import ValidationError
import re
import hashlib

def ip_validate(value):
    pattern=re.compile(r'^([12]?\d{1,2}\.){3}([12]?\d{1,2})$')
    if pattern.search(value) == None:
        raise ValidationError('ip格式错误')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'user','name':'user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','name':'password'}))

class HostInfo(forms.Form):
    hostname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': u'主机'}),
        error_messages={'required': u'主机名不能为空'})
    ip = forms.CharField(
        validators=[ip_validate,],
        widget=forms.TextInput(attrs={'placeholder': u'ip地址'}),
        error_messages={'required': u'ip不能为空'})
    host_group = forms.IntegerField(
        widget=forms.Select()
    )
    def __init__(self, *args, **kwargs):
        super(HostInfo, self).__init__(*args, **kwargs)
        self.fields['host_group'].widget.choices = models.HostGroup.objects.all().values_list('id', 'host_group_name')

class QueryInfo(forms.Form):
    hostname = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': u'主机'}),
        )
    ip = forms.CharField(
        required=False,
        validators=[ip_validate,],
        widget=forms.TextInput(attrs={'placeholder': u'ip地址'}),
        )
    host_group = forms.IntegerField(
        widget=forms.Select()
    )
    def __init__(self, *args, **kwargs):
        super(QueryInfo, self).__init__(*args, **kwargs)
        self.fields['host_group'].widget.choices = models.HostGroup.objects.all().values_list('id', 'host_group_name')


def login(request):
    obj = LoginForm(request.POST)
    if request.method == "POST":
        if obj.is_valid():
            all_data = obj.clean()
            login_username = all_data['username']
            hash_md5 = hashlib.md5()
            hash_md5.update(all_data['password'])
            login_password = (hash_md5.hexdigest())
            login_result = models.User_Login.objects.filter(username=login_username, password=login_password)
            if login_result.exists() == True:
                request.session['IS_LOGIN'] = True
                request.session['USRNAME'] = login_username
                return redirect("/app01/index/")
            else:
                return render(request, 'login.html', {'obj': obj, 'login_result': '用户名或密码错误',})
        else:
            error = obj.errors
            return render(request, 'login.html', {'obj': obj, 'error': error})
    return render(request, 'login.html', {'obj': obj})

def index(request):

    render(request,'index.html')

#添加
def add(request):
    obj = HostInfo(request.POST)
    if request.method == "POST":
        if obj.is_valid():
            all_data = obj.clean()
            print(all_data)
            h=models.Host.objects.get(hostname=all_data['hostname'],ip=all_data['ip'])
            g=models.HostGroup.objects.get(id=all_data['host_group'])
            g.host_set.add(h)
        else:
            error = obj.errors
            return render(request, 'add.html', {'obj': obj, 'error': error})
    return render(request, 'add.html', {'obj': obj})

#删除
def remove(request):
    obj = HostInfo(request.POST)
    if request.method == "POST":
        if obj.is_valid():
            all_data = obj.clean()
            print(all_data)
            h=models.Host.objects.get(hostname=all_data['hostname'],ip=all_data['ip'])
            g=models.HostGroup.objects.get(id=all_data['host_group'])
            g.host_set.remove(h)
        else:
            error = obj.errors
            return render(request, 'remove.html', {'obj': obj, 'error': error})
    return render(request, 'remove.html', {'obj': obj})

#查询
def query(request):
    obj = QueryInfo(request.POST)
    if request.method == "POST":
        if obj.is_valid():
            all_data = obj.clean()
            host_group=all_data['host_group']
            print(all_data)
            if all_data['hostname'] =='':
                del all_data['hostname']
            if all_data['ip'] =='':
                del all_data['ip']
            del all_data['host_group']
            print(all_data)
            h=models.Host.objects.get(**all_data)
            print h.host_group.all()
            group_list=[]
            for i in  h.host_group.all():
                group_list.append(i.host_group_name)
            print(group_list)
            return render(request, 'query.html', {'obj': obj, 'group_lsit': group_list})
        else:
            error = obj.errors
            return render(request, 'query.html', {'obj': obj, 'error': error})
    return render(request, 'query.html', {'obj': obj})


def ip_list(request):
    host_obj = models.Host.objects.all()
    h=models.Host.objects.get(hostname='h4')
    for i in  h.host_group.all():
        print i.host_group_name
    return render(request, 'ip_list.html', {'host_obj':host_obj,})