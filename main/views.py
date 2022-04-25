from django.http import HttpResponseNotFound
from django.shortcuts import render

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def base(request):
    return render(request, 'main/home.html')