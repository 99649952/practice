#coding:utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from app01 import models
import hashlib


def index(request):
    return render(request, 'index.html',)

def login(request):
    if request.method == "POST":
        input_user = request.POST['user']
        input_password = request.POST['password']
        hash_md5 = hashlib.md5()
        hash_md5.update(input_password)
        md5_password = (hash_md5.hexdigest())
        login_result = models.UserInfo.objects.filter(username=input_user, password=md5_password)
        if login_result.exists() == True:
            print(login_result.exists())
            return redirect("/index/")
        else:
            return render(request, 'login.html', {'login_result': '用户名或密码错误'})
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        input_user = request.POST['user']
        input_password = request.POST['password']
        hash_md5 = hashlib.md5()
        hash_md5.update(input_password)
        md5_password = (hash_md5.hexdigest())
        user_info = models.UserInfo.objects.filter(username=input_user)
        if user_info.exists() == True:
            return render(request, 'register.html', {'register_result': '用户名已存在'})
        else:
            models.UserInfo.objects.create(username=input_user, password=md5_password)
            return render(request, 'login.html',)
    return render(request, 'register.html')

def user_manager(request):
    user_info_list = models.UserInfo.objects.all()
    for i in user_info_list:
        print(i.username, i.password,)
    return render(request, 'manager.html', {'user_info_list': user_info_list})