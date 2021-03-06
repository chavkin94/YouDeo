from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

# используется если не связанно с моделью
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label='URL')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'row': 10}), label='Содержание статьи')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True) #required делает поле не обязательным, initial делает поле по умолчанию отмеченным
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label="Категория не выбрана")


# используется когда связанно с моделью
class AddPostForm(forms.ModelForm):
    #конструктор для того чтобы в списке сделать нулевое значение
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        # fields = '__all__'  #какие поля нужно отобразить в форме в данном случае все
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
           'title': forms.TextInput(attrs={'class': 'form-input'}),
           'content': forms.Textarea(attrs={'cols': 60, 'row': 10}),
        }

    # Валидация данных по полю title
    def clean_title(self):
        title = self.cleaned_data['title'] # получаем данные по заголовку
        if len(title) >200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class RegisterUserForm(UserCreationForm):
    # штуки для того чтобы сделать стильными поля в форме
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # нужен был при стандартном выводе
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        # }