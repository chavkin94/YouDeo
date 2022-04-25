from django.apps import AppConfig


class WomenConfig(AppConfig):
    name = 'women'
    verbose_name = 'Женщины мира' #{ наименование группы (заглавие типа пользователи и группы) в админке , работает если только в setting в свойстве INSTALLED_APPS прописывать приложение типа women.apps.WomenConfig}#
