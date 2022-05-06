from django.urls import path
from django.contrib import auth
from . import views
from .views import *

app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='account-login-user'),
    # path('logout/', views.user_login, name='account-logout-user'),
    # path('registration/', RegisterUser.as_view(), name='account-registration-user'),
    # path('login/', auth.views.login, name='login'),
    # path('logout/', auth.views.logout, name='logout'),
    # path('logout-then-login/' auth.views.logout_then_login, name='logout_then_login'),
    # path('', views.dashboard, name='dashboard'),
    # path('account/', views.account2, name='account_account'),
    path('<slug:slug>/', AccountShow.as_view(), name='account'),
    path('<slug>/edit', AccountUpdate.as_view(), name='edit'),
]