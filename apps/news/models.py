from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news/', help_text="Изображение в формате PNG")
    short_text_en = models.CharField(max_length=255, help_text="short text news")
    short_text_ru = models.CharField(max_length=255, help_text="Короткий текст новости")
    is_displayed = models.BooleanField('Показать')
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.short_text_ru[:50]  # Обрезаем текст для отображения
