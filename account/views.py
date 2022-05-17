from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, UpdateView
from account.forms import *
from account.models import AccountTopImage


class AccountShow(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'account/account.html'
    context_object_name = 'account'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователь'
        return context


class AccountShow(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'account/account.html'
    context_object_name = 'account'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователь'
        return context

# @login_required
# def account_edit(request, slug):
#     account = get_object_or_404(User, username=slug)
#     if request.method == 'POST':
#         form = AccountForm(request.POST, request.FILES, instance=account)
#         if form.is_valid():
#             account = form.save()
#             return redirect('account:show')
#     else:
#         form = AccountForm(instance=account)
#     context = {'form': form}
#     return render(request, 'account/account_editing.html', context)


class AccountImageUpdate(DetailView):
    model = AccountTopImage

    template_name = 'account/account_image.html'
    fields = ['photo']
