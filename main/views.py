from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render


# from main.models import ServiceCategory
#
# menu = [{'title': "Лента", 'url_name': 'feed'},
#         {'title': "Поиск мастера", 'url_name': 'home'},
#         {'title': "Сообщения", 'url_name': 'message'},
#         {'title': "Профиль", 'url_name': 'account'},
#         {'title': "Поиск мастера", 'url_name': 'account'},
#         ]
#
#
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


#
#
# # def base(request):
# #     return render(request, 'main/content/home.html', {'title': 'Профиль'})
#
# def show_home(request):
#     service_category = ServiceCategory.objects.all()
#
#     if len(service_category) == 0:
#         raise Http404()
#     context = {
#         # 'posts': posts,
#         'service_category': service_category,
#         'title': 'Профиль',
#         # 'cat_selected': cat_id
#     }
#     return render(request, 'main/content/home.html', context=context)


def index(request):
    return render(request, 'main/content/index.html', {'title': 'Профиль'})


def account(request):
    return render(request, 'main/content/account.html', {'title': 'Профиль'})


def feed(request):
    return render(request, 'main/content/feed.html', {'title': 'Публикации'})


def search(request):
    return render(request, 'main/content/search.html', {'title': 'Поиск мастера'})


def message(request):
    return render(request, 'main/content/message.html', {'title': 'Сообщения'})


def master(request):
    return render(request, 'main/content/master.html', {'title': 'Профиль мастера'})


def organization(request):
    return render(request, 'main/content/organization.html', {'title': 'Профиль организации'})
