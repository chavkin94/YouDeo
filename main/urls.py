from django.urls import path
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path(r'', views.base, name='home'),
    path(r'account/', views.account, name='account'),
    path(r'feed/', views.feed, name='feed'),
    path(r'message/', views.message, name='message'),
    path(r'master/', views.master, name='master'),
    path(r'organization/', views.organization, name='organization'),
]
