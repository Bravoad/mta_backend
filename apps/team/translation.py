from modeltranslation.translator import translator, TranslationOptions
from .models import Team


class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'staff')


translator.register(Team, TeamTranslationOptions)
