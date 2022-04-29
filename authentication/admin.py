from django.contrib import admin

from authentication.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_active')
    # list_display_links = ('') #{ поля на которые можно кликать}#
    # search_fields = ('fk_user') #{ по каким полям можно производить поиск}#
    # list_filter = ('fk_user', 'time_create', 'time_update') #{поля по которым можно сортировать админку}#


admin.site.register(User, UserAdmin)


# admin.site.register(User)
