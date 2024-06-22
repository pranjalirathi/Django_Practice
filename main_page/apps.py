from django.apps import AppConfig

# changed the default setting from StaticFiles to MainPageConfig name due to settings.py
class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_page'
