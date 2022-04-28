from django.db.models import Count

from .models import *
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        # {'title': "Войти", 'url_name': 'login'}
]


class DataMixin:
        paginate_by = 2
        def get_user_context(self, **kwargs):
                context = kwargs

                # cats = Category.objects.all() #если нужно выбрать все
                cats = Category.objects.annotate(Count('women')) #сделали так для того чтобы убрать те категории у которых нет постов
                # использовалось когда нужно отображать все
                # context['menu'] = menu
                user_menu = menu.copy()
                if not self.request.user.is_authenticated: #если пользователь не авторизован
                        user_menu.pop(1)  # удаляем второй пункт
                context['menu'] = user_menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context
