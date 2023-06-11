from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend"
    verbose_name = "Основное"

    def ready(self) -> None:
        import backend.signals
