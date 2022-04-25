from django import template
from women.models import *

register = template.Library()

# простой тег - коллекция данных
@register.simple_tag(name='getcats') #{ дкоратор чтобы превратить функцию в тег который можно использовать в шаблонах приложения, если нужно обращаться к тегу не по имени функции а по другому имени в скобках декоратора указать имя}#
def get_categories(filter=None): #{Функция для простого тега, в скобках параметры которые передаются, можно без них (в данном случае filter, без него в теле был бы только ретен)}#
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


# включающий тег позволяет дополнительно строить свой собственный шаблон и возвращать фрагмент HTML страницы
@register.inclusion_tag('women/list_categories.html') #шаблоны можно хранить не в общей куче а в отдельной папке
def show_categories(sort=None, cat_selected=0): # данные автомотически передаются вышеуказанному шаблону
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}
