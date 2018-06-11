# -*- coding:utf-8 -*-
from django.conf.urls import url
from  . import views

#设置命名空间
app_name = 'wechat'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    #url(r'^$', views.index, name='index'),
]