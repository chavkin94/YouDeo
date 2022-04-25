from django.urls import path
from django.contrib import auth
from . import views

urlpatterns = [
    path('login/', views.user_login, name='account-login-user'),
    path('logout/', views.user_login, name='account-logout-user'),
    # path('registration/', RegisterUser.as_view(), name='account-registration-user'),
    # path('login/', auth.views.login, name='login'),
    # path('logout/', auth.views.logout, name='logout'),
    # path('logout-then-login/' auth.views.logout_then_login, name='logout_then_login'),
    # path('', views.dashboard, name='dashboard'),
]