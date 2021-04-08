from django.db import models

class product(models.Model):
    name = models.CharField('Имя', max_length = 150)
    price = models.FloatField('Цена')
    description = models.TextField('Описание')
    count = models.IntegerField('Количество')
    is_active = models.BooleanField('Есть в наличии')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class category(models.Model):
    name = models.CharField('Имя', max_length = 50)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'