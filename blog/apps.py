"""App config"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """The name of the app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
