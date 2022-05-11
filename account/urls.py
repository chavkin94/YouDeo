from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('<slug:slug>/', AccountShow.as_view(), name='account'),
    path('<slug:slug>/edit', AccountUpdate.as_view(), name='edit'),
]