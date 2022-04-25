from django.urls import path
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('', views.base, name='home'),
]
