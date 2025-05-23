from django.apps import AppConfig


class PartnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.partner'

    def ready(self):
        import apps.partner.translation
