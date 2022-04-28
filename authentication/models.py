from django.conf import settings
from django.db import models

type_gender = ['мужской','женский']


class UserDetails(models.Model):
    g_null = ''
    men = 'м'
    women = 'ж'
    gender_choices = [
        (g_null, ''),
        (men, 'мужской'),
        (women, 'женский'),
    ]
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Пользователь")
    birthday = models.DateField(verbose_name="Дата рождения")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    gender = models.CharField(choices=gender_choices, max_length=30, verbose_name="Пол", default=g_null,)
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")

    class Meta:
        verbose_name = 'Подробности о пользователе'
        verbose_name_plural = 'Подробности о пользователях'
