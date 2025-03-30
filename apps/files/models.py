from django.db import models


class Files(models.Model):
    file = models.FileField()
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
