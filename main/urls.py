from django.urls import path, include
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('', views.index, name='main_home'),
    path('login', views.index, name='main_login'),
    path('account1/', views.account1, name='main_account1'),
    path('feed/', views.feed, name='main_feed'),
    path('search/', views.search, name='main_search'),
    path('message/', views.message, name='main_message'),
    path('master/', views.master, name='main_master'),
    path('organization/', views.organization, name='main_organization'),
]
