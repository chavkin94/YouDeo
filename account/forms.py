from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm

from authentication.models import User


class EditAccountForm(ModelForm):
    # username = forms.CharField(label='Логин на сайте', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # gender = forms.ChoiceField(label='Пол', widget=forms.Select(attrs={'class': 'form-control'}), choices=(('', ""), ('м', "мужской"), ('ж', "женский")))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'birthday', 'gender', 'email', 'phone_number']

    # widgets = {
    #     'username': forms.TextInput(attrs={'class': 'form-input'}),
    #     'first_name': forms.Textarea(attrs={'cols': 60, 'row': 10}),
    # }