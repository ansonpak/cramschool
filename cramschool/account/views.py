from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required  
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from account.models import User
from account.forms import UserForm
from main.views import admin_required    


@admin_required
def register(request):
    template = 'account/register.html'
    if request.method=='GET':
        return render(request, template, {'userForm':UserForm()})
    # request.method == 'POST':
    userForm = UserForm(request.POST)
    
    user = userForm.save()
    user.set_password(user.password)
    user.save() 
    messages.success(request, '歡迎註冊')
    return redirect('main:main')


def login(request):
    template = 'account/login.html'
    if request.method=='GET':
        return render(request, template)
    # request.method=='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        messages.error(request, '請輸入資料')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user: # authenticate fail
        messages.error(request, '登入失敗')
        return render(request, template)
    if not user.is_active:
        messages.error(request, '帳號已停用')
        return render(request, template)
    # login success
    auth_login(request, user)
    messages.success(request, '登入成功')
    return redirect('main:main')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '登出成功')
    return redirect('main:main')