from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import *
from authentication.utils import DataMixin


def login(request):
    return render(request, 'authentication/login.html', {'title': 'Войти'})


def registration(request):
    return HttpResponse("Регистрация")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    #перекидывает на указанный адрес при авторизации успешной
    def get_success_url(self):
        return reverse_lazy('main_home')
# @login_required
# @transaction.atomic
# def update_user(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         user_details_form = UserDetailsForm(request.POST, instance=request.user.user_details)
#         if user_form.is_valid() and user_details_form.is_valid():
#             user_form.save()
#             user_details_form.save()
#             messages.success(request, ('Ваш профиль был успешно обновлен!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, ('Пожалуйста, исправьте ошибки.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         user_details_form = UserDetailsForm(instance=request.user.profile)
#     return render(request, 'registration.html', {
#         'user_form': user_form,
#         'user_details_form': user_details_form
#     })

def logout_user(request):
    logout(request)
    return redirect("authentication_login")