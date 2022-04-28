from django.contrib import admin
from .models import *


# class ServiceCategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'service_description')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     prepopulated_fields = {"slug": ("name",)}
#
#
# admin.site.register(ServiceCategory, ServiceCategoryAdmin)
