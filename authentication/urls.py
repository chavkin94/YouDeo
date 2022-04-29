from django.urls import path, include
from . import views
from django.contrib.auth.views import auth_login

from .views import *

urlpatterns = [
    path('login/', views.login, name='authentication_login'),
    path('login/', views.login, name='authentication_register'),
    # path('register/', RegisterUser.as_view(), name='authentication_register'),
]
