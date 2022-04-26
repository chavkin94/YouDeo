from django.http import HttpResponseNotFound
from django.shortcuts import render


menu = [{'title': "Публикации", 'url_name': 'lenta'},
        {'title': "Поиск мастера", 'url_name': 'search'},
        {'title': "Сообщения", 'url_name': 'message'},
        {'title': "Профиль", 'url_name': 'account'},
        {'title': "Профиль мастера", 'url_name': 'master'},
        {'title': "Профиль организации", 'url_name': 'organization'}
        ]


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def base(request):
    return render(request, 'main/content/home.html', {'title': 'Поиск мастера'})


def account(request):
    return render(request, 'main/content/account.html', {'title': 'Профиль'})


def feed(request):
    return render(request, 'main/content/feed.html', {'title': 'Публикации'})


def message(request):
    return render(request, 'main/content/message.html', {'title': 'Сообщения'})


def master(request):
    return render(request, 'main/content/master.html', {'title': 'Профиль мастера'})


def organization(request):
    return render(request, 'main/content/organization.html', {'title': 'Профиль организации'})
