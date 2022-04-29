from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView # detailviews отвечает за отображение какого либо поста (show_post)
from django.contrib.auth.mixins import LoginRequiredMixin #Миксин который проверяет пользователя на авторизацию, работает только с классами представлений, если хотим работать с функцией, уже нужно исплльзовать декоратор
from .forms import *
from . models import *
from .utils import *

# Раньше было здесь
# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
#         ]

#лкассы представлений заменил index
class WomenHome(DataMixin, ListView):

    model = Women #отображает все записи
    template_name = 'women/index.html' #чтобы задать уникальный файл
    context_object_name = 'posts'  # чтобы использовать свое наименование переменной , а не object_list
    # extra_context = {'title': 'Главная страница'} # можно передавать только статические данные

    def get_context_data(self, *, object_list=None, **kwargs): #позволяет передовать не только статические но и динамические данные
        context = super().get_context_data(**kwargs)
        # До убирания дублирования
        # context['menu'] = menu
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        c_def = self.get_user_context(title="Главная страница") # Миксины чтобы убрать дублирование кода
        # context = dict(list(context.items()) + list(c_def.items())) # Формирование общего словаря
        return dict(list(context.items()) + list(c_def.items()))

    # позволяет отображать не все данные , а только те что публекуются
    def get_queryset(self):
        return Women.objects.filter(is_published=True)


#заменили на классы представлений
# def index(request):
#     posts = Women.objects.all()
#     # cats = Category.objects.all() так как код повторялся перенесли в тег
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#     return render(request, 'women/index.html', context=context)

# @login_required # делает доступной только для зарегистрированных пользователей
def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj,'menu':menu, 'title': 'О сайте'})
    # return render(request, 'women/about.html', {'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home') #штука с которой нужно разобраться что то с get_absolyte
    login_url = reverse_lazy('admin') #штука, которая перекидывает пользователя если он не авторизован
    raise_exception = True # если мы не хотим перенапровлять неавторизованного пользователя, а хотим отображать 403 (доступ запрещен), можно без него

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Добавление статьи'
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))
        # return context
# использовалось до представления
# def addpage(request):
#     #можно делать одной строкой form = AddPostForm(), но для того чтобы данные при неправильном заполнении сохранялись нужно делать так
#     # form = AddPostForm() #класс из файла forms в корне приложения
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)  # request.FILES необходимо для того чтобы передать изображение из формы
#         if form.is_valid():
#             # print(form.cleaned_data)
#             #фрагмент сохранения в базу несвязанной формы с моделью и обработка ошибки сохранения, в связанной проверки на ошибки происходят автоматически
#             # try:
#             #     Women.objects.create(**form.cleaned_data) # строка сохранения данных если не связана форма с моделью
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Контакты")


# def login(request):
#     return HttpResponse("Вход")

# Пример использования без slug
# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")


#использовалось до применения представлений
# пример использования с slug, так лучше делать для поисковиков
# def show_post(request, post_slug):
#     # post = get_object_or_404(Women, pk=post_id) использовалось когда использовали id а не slug, кроме того нужно поправить в модели get_absolut_url и урлс
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context=context)

#
class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug' #позволяет изменить наименование переменной slug на другое, аналогично для ключа, только pk
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = context['post']
        # return context
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # обработчик ошибок если такой страницы не найдено, то 404


    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # return context
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# до применения классов редставлений
# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id
#     }
#     return render(request, 'women/index.html', context=context)

# def categories(request, catid):
#     # if(request.Get):
#     #     print(request.Get)
#     # if int(catid) >400:
#     #     raise Http404()   #Ошибка 404
#     # if int(catid) >4:
#     #     return redirect('home', permanent=True) #перенаправляет на главную (постоянно true)
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{ catid }</p>")
#
# def archive(request, year):
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{ year }</p>")

class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) # при успешной регистрации сразу происходит вход автоматически
        return redirect('home')



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    #перекидывает на указанный адрес при авторизации успешной
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
