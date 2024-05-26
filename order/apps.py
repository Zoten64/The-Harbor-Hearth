"""App configuration"""
from django.apps import AppConfig


class OrderConfig(AppConfig):
    """App name"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'
