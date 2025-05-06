from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news/', help_text="Изображение в формате PNG")
    short_text = models.CharField(max_length=255, help_text="Краткий текст новости", default='')
    is_displayed = models.BooleanField('Показать', default=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.short_text[:50]
