# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def register(request):
    #从 get 或者 post 请求中获取next 参数值
    # get 请求中 next 通过 url 传递，即 /?next = value
    # post 请求中，next 通过表单传递，即<input type='hidden' name='text' value='{{ next }}'/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        #实例化一个用户注册表单数据
        form = RegisterForm(request.POST)
        #验证数据的合法性
        if form.is_valid():
            form.save()
            #注册成功，跳转回首页
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        #不是post请求，展示一个空的注册表单给用户
        form = RegisterForm()
        # 渲染模板
        # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
        # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return  render(request, 'wechat/register.html', context={'form':form,'next':redirect_to})

def index(request):
    return render(request, 'index.html')

def send(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        #tulps = eval(email)
        #print(tulps)
        msg='你收到这封邮件是因为你请求重置你在网站 127.0.0.1:8000上的用户账户密码。请访问该页面并选择一个新密码：<a href="http://127.0.0.1:8000/wechat/reset/NA/4n8-64ab7ff92254d18c6b15/">http://127.0.0.1:8000/users/reset/NA/4n8-64ab7ff92254d18c6b15/</a><br/>你的用户名，如果已忘记的话： admin</br>感谢使用我们的站点！<br/>127.0.0.1:8000 团队'
        send_mail('测试邮件01',
                  msg,
                  settings.EMAIL_FROM,
                  [email])
    return  render(request, 'registration/password_reset_done.html')




