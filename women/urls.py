from django.urls import path, re_path
from .views import *


urlpatterns = [
    #когда не использовали класс представлений
    # path('', index, name='home'),
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    #использовалось до представлний
    # path('addpage', addpage, name='add_page'),
    path('addpage', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login', login, name='login'),
    # path('post/<int:post_id>/', show_post, name='post'),  Использовалось без слагов, по id, правильнее использовать слаги
    # использовалось до применения представления
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    #до применения класса представлений
    # path('category/<int:cat_id>/', show_category, name='category'),

    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})', archive)
]