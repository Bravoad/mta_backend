from django.db import models


class Partner(models.Model):
    name = models.CharField('Наименование партнера', max_length=255, default='')
    logo = models.ImageField('логотип')
    order = models.PositiveIntegerField('порядок')
    is_displayed = models.BooleanField('Показать')

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return self.name_ru
