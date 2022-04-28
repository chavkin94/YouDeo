from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# class ServiceCategory(models.Model):
#     name = models.CharField(max_length=100, db_index=True, verbose_name="Категория услуг")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
#     time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
#     service_category_description = models.TextField(blank=True, verbose_name="Описание категории услуг")
#     is_published = models.BooleanField(default=True, verbose_name="Публикация")
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('category', kwargs={'cat_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Категория услуг'
#         verbose_name_plural = 'Категории услуг'
#         ordering = ['id']

# class Services(models.Model):
#     name = models.CharField(max_length=100, db_index=True, verbose_name="Услуга")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     service_description = models.TextField(blank=True, verbose_name="Описание услуг")
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
#     time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
#     is_published = models.BooleanField(default=True, verbose_name="Публикация")
#     cat = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT, verbose_name="Категория услуг")
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('category', kwargs={'cat_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Категория услуг'
#         verbose_name_plural = 'Категории услуг'
#         ordering = ['id']
