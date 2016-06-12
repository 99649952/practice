#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
from django.shortcuts import render
from django import forms
import models
from django.core.exceptions import ValidationError
import re

def ip_validate(value):
    pattern=re.compile(r'^([12]?\d{1,2}\.){3}([12]?\d{1,2})$')
    if pattern.search(value) == None:
        raise ValidationError('ip格式错误')



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



def index(request):
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
            return render(request, 'index.html', {'obj': obj, 'error': error})
    return render(request, 'index.html', {'obj': obj})

def ip_list(request):
    host_obj = models.Host.objects.all()
    return render(request,'ip_list.html',{'host_obj':host_obj, })