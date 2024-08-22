from django.apps import AppConfig


class BarbercutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barbercut'
    verbose_name = 'Записи клиентов'
    
    def ready(self):
        import barbercut.signals
