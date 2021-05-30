from django.contrib import admin
from django.urls import path
from . import views
#from mainapp import views
import os

urlpatterns = [
    path('',views.Index, name='Index'),
    path('register/',views.register),
    path('register/reg_done/',views.reg_done),
    path('senddata',views.senddata),
    path('login/',views.login),
    path('online/',views.online),
    path('one/',views.one),
    path('one2/',views.one2),
    path('one3/',views.one3),
    path('one4/',views.one4),
    path('one5/',views.one5),
    path('quiz/',views.quiz),
    path('login/log_done/',views.log_done),
    path('home/', views.home),  

] 