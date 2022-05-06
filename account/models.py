from django.db import models

# class Account(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Заголовок")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")# slug необходим для поисковых роботов
#     content = models.TextField(blank=True, verbose_name="Текст статьи")
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
#     time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
#     is_published = models.BooleanField(default=True, verbose_name="Публикация")
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")  # в название поля джанго сам добавит _id
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('post', kwargs={'post_slug': self.slug}) #{штука для того чтобы делать ссылки правильно. Кроме этого добавляет кнопкц смотреть страницу в админке}#
#
#     class Meta:
#         verbose_name = 'Известная женщина'
#         verbose_name_plural = 'Известные женщины'
#         ordering = ['-time_create', 'title'] #{ сортировка применяется как на админку, так и на отображение строк при использовании all на самом сайте}#

class AccountTopImage(models.Model):
title = models.CharField(max_length=255, verbose_name="Заголовок")