from modeltranslation.translator import translator, TranslationOptions
from .models import Brand


class BrandTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'short_description',
        'dynamic_description',
    )


translator.register(Brand, BrandTranslationOptions)
