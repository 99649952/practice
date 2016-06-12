#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
import re
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': "form-control", "placeholder":"用户名"})
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': "form-control", "placeholder":"密码"})
    )

def ip_validata(self):
    ip_re = re.compile(r'([12]?\d{1,2}\.){3}([12]?\d{1,2})')
    if not ip_re:
        raise ValidationError('ip格式输入错误')

class Asset_Form(forms.Form):

    serial_number = forms.CharField(
        error_messages={'required': u'序号不能为空'},
        widget=forms.widgets.TextInput(attrs={'class': "form-control", "placeholder":"序号" ,'name':'serial_number'})
    )

    business_ip = forms.CharField(
        error_messages={'required': u'业务IP不能为空'},
        validators=[ip_validata,],
        widget=forms.widgets.TextInput(attrs={'class': "form-control", "placeholder":"业务IP",'name':'business_ip'})
    )

    manage_ip = forms.CharField(
        error_messages={'required': u'管理IP不能为空'},
        widget=forms.widgets.TextInput(attrs={'class': "form-control", "placeholder":"管理IP",'name':'manage_ip'})
    )

    remark = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': "form-control", "placeholder":"备注",'name':'remark'})
    )

