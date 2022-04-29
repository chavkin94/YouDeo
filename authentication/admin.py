from django.contrib import admin
from authentication.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_active')
    list_display_links = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_active')


admin.site.register(User, UserAdmin)

