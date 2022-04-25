from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') #{ список полей которые хотим видеть в админке}#
    list_display_links = ('id', 'title') #{ поля на которые можно кликать}#
    search_fields = ('title', 'content') #{ по каким полям можно производить поиск}#
    list_editable = ('is_published',) #{список полей которые можно редактировать во всем списке не переходя в отдельную строку}#
    list_filter = ('is_published', 'time_create') #{поля по которым можно сортировать админку}#
    prepopulated_fields = {"slug": ("title",)} #чтобы заполнять slug автомотически транслейтом поля title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) #{ так как поиск по одному полю в конце необходимо поставить запятую,чтоб воспринимал как картеж}#
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Women, WomenAdmin)  #{ можно без второго параметра}#
admin.site.register(Category, CategoryAdmin)
