# coding:utf-8
from cmdb import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from cmdb import models
import json


def login(request):
    login_form = forms.LoginForm()
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.clean()
            # 如果登录成功，写入session，跳转index
            if data['username'] == 'lxb' and data['password'] == 'l123456':
                request.session['IS_LOGIN'] = True
                request.session['USRNAME'] = 'lxb'
                return redirect('/cmdb/home/')
        else:
            error_msg = login_form.errors.as_data()
            return render(request, 'account/login.html', {'login_form': login_form, 'errors': error_msg})
    return render(request, 'account/login.html', {'model': login_form})

def home(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USRNAME', False)
        return render(request, 'home/index.html', {'username': username})
    else:
        return redirect("/cmdb/login/")

#没有session，index默认跳转到登录页面
def index(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USRNAME', False)
        return render(request, 'home/index.html', {'username': username})
    else:
        return redirect("/cmdb/login/")

def lists(request):
    assets_list = models.Assets.objects.all()
    return render(request, 'asset/lists.html', {'user_info_list': assets_list})

def add(request):
    asset_form = forms.Asset_Form()
    if request.method == "POST":
        user_input_obj = forms.Asset_Form(request.POST)
        if user_input_obj.is_valid():
            data = user_input_obj.clean()
            models.Assets.objects.create(serial_number=data['serial_number'], business_ip=data['business_ip'],
                                           manage_ip=data['manage_ip'],status='start')
            return redirect('/cmdb/lists/',)
        else:
            error_msg = user_input_obj.errors.as_data()
            return render(request, 'asset/import_single.html', {'model': asset_form, 'errors': error_msg})
    return render(request, 'asset/import_single.html', {'model': asset_form})

def asset_modify(request):
    asset_data = json.loads(request.POST['data'])
    for i in asset_data:
        serial_number = i['serial_number']
        business_ip = i['business_ip']
        manage_ip = i['manage_ip']

        models.Assets.objects.filter(serial_number=serial_number).update(business_ip=business_ip,manage_ip=manage_ip)
    return HttpResponse('xxxxxxxxxxxxxxxxxxxxxx')