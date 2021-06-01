from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'cms_dashboard'
    verbose_name = 'CMS Dashboard'
    identifier_pattern = None
