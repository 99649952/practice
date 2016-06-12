# -*-coding:utf-8-*-
from django.shortcuts import render,redirect
import forms
import hashlib
import models
import datetime
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#登录认证session写入
def login(request):
    obj = forms.LoginForm(request.POST)
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
                return redirect("/")
            else:
                return render(request, 'account/login.html', {'obj': obj, 'login_result': '用户名或密码错误',})
        else:
            error = obj.errors
            return render(request, 'account/login.html', {'obj': obj, 'error': error})
    return render(request, 'account/login.html', {'obj': obj})

#注册
def register(request):
    if request.method == "POST":
        input_user = request.POST['user']
        input_password = request.POST['password']
        hash_md5 = hashlib.md5()
        hash_md5.update(input_password)
        md5_password = (hash_md5.hexdigest())
        user_create = models.User_Login.objects.get_or_create(username=input_user,password=md5_password)
        if user_create[1] == False:
            return render(request, 'account/register.html', {'register_result': '用户名已存在'})
        else:
            return redirect('/login/')
    return render(request, 'account/register.html')

#首页
def index(request):
    is_login = request.session.get('IS_LOGIN', False)
    articles = models.Article.objects.all()
    if is_login:
        username = request.session.get('USRNAME', False)
        user = models.UserInfo.objects.get(username__username=username).user
        request.session['USER'] = user
        return render(request, 'index/index.html', {'is_login':is_login,'articles': articles,'username': user})
    return render(request,'index/index.html', {'articles': articles,})

#注销
def logout(request):
    request.session.flush()
    return redirect('/')

#分类处理
def category(request,category_id):
    articles = models.Article.objects.filter(pk=category_id) #主键id
    return render(request,'index/index.html',{'articles': articles})

def article_detail(request,article_id):
    try:
        article_obj = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request,'404.html',{'err_msg':u"文章不存在！"})
    return render(request,'article.html', {'article_obj':article_obj})

def new_article(request):
    if request.method == 'POST':
        user = request.session['USER']
        form = forms.ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            author = models.UserInfo.objects.get(user=user)
            category = models.Category.objects.get(pk=form_data['category'])
            form_data['author'] = author
            form_data['category'] = category
            # new_img_path = forms.handle_uploaded_file(request,request.FILES['head_img'])
            # form_data['head_img'] = new_img_path
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return redirect('/')
        else:
            print('err:',form.errors)
    return redirect('/')

