from django.apps import AppConfig
from django.contrib.auth.models import Group
from django.conf import settings


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

