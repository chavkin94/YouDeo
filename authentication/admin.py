from django.contrib import admin
from authentication.models import UserDetails


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('fk_user', 'birthday', 'time_create', 'time_update', 'gender', 'phone_number')
    # list_display_links = ('') #{ поля на которые можно кликать}#
    # search_fields = ('fk_user') #{ по каким полям можно производить поиск}#
    list_filter = ('fk_user', 'time_create', 'time_update') #{поля по которым можно сортировать админку}#


admin.site.register(UserDetails, UserDetailsAdmin)
