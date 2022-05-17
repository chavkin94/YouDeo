from django.contrib import admin

from account.models import AccountTopImage


class AccountTopImageAdmin(admin.ModelAdmin):
    list_display = ('account_fk', 'photo') #{ список полей которые хотим видеть в админке}#

admin.site.register(AccountTopImage, AccountTopImageAdmin)