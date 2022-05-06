from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='authentication_login'),
    path('logout/', logout_user, name='authentication_logout'),
    path('register/', RegisterUser.as_view(), name='authentication_register'),
]
