from django.db import models

# Create your models here.
class Team(models.Model):
    name_en = models.CharField('full_name', max_length=255)
    name_ru = models.CharField('Наименование', max_length=255)
    staff_en = models.CharField('staff', max_length=255)
    staff_ru = models.CharField('Должность', max_length=255)
    picture = models.ImageField('Портрет')
    order = models.PositiveIntegerField('Порядок')
    is_displayed = models.BooleanField('Показать')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
