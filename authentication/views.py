from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import RegisterUserForm
from authentication.utils import DataMixin


def login(request):
    return HttpResponse("Вход")


def registration(request):
    return HttpResponse("Регистрация")


class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))