from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('<slug:slug>/', AccountShow.as_view(), name='show'),
    path('<slug:slug>/account_change/', account_edit, name='edit'),
    path('<slug:slug>/account_image_edit/', AccountImageUpdate.as_view(), name='image_edit'),

]