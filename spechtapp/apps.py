from django.apps import AppConfig


class SpechtappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spechtapp'

    def ready(self):
        import spechtapp.signals
