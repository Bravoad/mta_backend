from django.db import models


class Team(models.Model):
    name = models.CharField('Имя сотрудника', max_length=255, default='')
    staff = models.CharField('Должность', max_length=255, default='')
    picture = models.ImageField('Портрет')
    order = models.PositiveIntegerField('Порядок')
    is_displayed = models.BooleanField('Показать', default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['order']

    def __str__(self):
        return self.name
