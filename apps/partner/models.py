from django.db import models

# Create your models here.
class Partner(models.Model):
    name_en = models.CharField('name partner', max_length=255)
    name_ru = models.CharField('Наименование партнера', max_length=255)
    logo = models.ImageField('логотип')
    order = models.PositiveIntegerField('порядок')
    is_displayed = models.BooleanField('Показать')

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return self.name_ru
