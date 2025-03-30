from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Brand(models.Model):
    name_en = models.CharField('full_name', max_length=255)
    name_ru = models.CharField('Наименование', max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField('Портрет')
    picture = models.ImageField('Картинка')
    brand_picture = models.ImageField('Картинка', blank=True, null=True)
    short_description_en = models.TextField('short description', default='')
    short_description_ru = models.TextField('Краткое описание', default='')
    dynamic_description = RichTextUploadingField(
        'Динамическое описание',
        blank=True,
        null=True,
        help_text='HTML-редактор, позволяющий вставлять изображения и текст в любом месте'
    )
    order = models.PositiveIntegerField('Порядок')
    recommended_brands = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        verbose_name='Рекомендуемые бренды',
        help_text='Выберите бренды, которые рекомендуются после описания данного бренда'
    )
    is_displayed = models.BooleanField('Показать')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_ru)  # или можно использовать name_en, в зависимости от предпочтений
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_ru
