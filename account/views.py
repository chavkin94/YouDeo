from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView
from account.forms import *



# def account2(request):
#     return render(request, 'account/account.html', {'title': 'Профиль'})

# User
class AccountShow(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'account/account.html'
    context_object_name = 'account'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователь'
        return context


class AccountUpdate(UpdateView):

    model = User
    slug_field = 'username'
    template_name = 'account/account_editing.html'
    fields = ['username', 'first_name', 'last_name', 'birthday', 'gender', 'email', 'phone_number']