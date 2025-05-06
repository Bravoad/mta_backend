from modeltranslation.translator import translator, TranslationOptions
from .models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('short_text',)


translator.register(News, NewsTranslationOptions)
