from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import *
from authentication.utils import DataMixin


# def login(request):
#     return render(request, 'authentication/login.html', {'title': 'Войти'})


# def registration(request):
#     return HttpResponse("Регистрация")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('authentication_login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'authentication/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    #перекидывает на указанный адрес при авторизации успешной
    def get_success_url(self):
        return reverse_lazy('main_home')

def logout_user(request):
    logout(request)
    return redirect('authentication_login')

