from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField('Наименование', max_length=255, default='')
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField('Логотип')
    picture = models.ImageField('Картинка')
    brand_picture = models.ImageField('Доп. Картинка', blank=True, null=True)
    short_description = models.TextField('Краткое описание', default='')
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
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
