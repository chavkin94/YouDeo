from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

type_gender = ['мужской','женский']

class User(AbstractUser):
    g_null = ''
    men = 'м'
    women = 'ж'
    gender_choices = [
        (g_null, ''),
        (men, 'мужской'),
        (women, 'женский'),
    ]
    birthday = models.DateField(verbose_name="Дата рождения", blank=True,null=True)
    gender = models.CharField(choices=gender_choices, max_length=30, verbose_name="Пол", default=g_null, blank=True,null=True)
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True,null=True)

    class Meta:
        verbose_name = 'Подробности о пользователе'
        verbose_name_plural = 'Подробности о пользователях'
