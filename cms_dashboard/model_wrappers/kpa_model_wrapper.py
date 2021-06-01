from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper


class KpaModelWrapper(ModelWrapper):

    model = 'bhp_personnel.keyperformancearea'
    querystring_attrs = ['contract', 'emp_identifier', ]
    next_url_attrs = ['contract', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract

    @property
    def kpa_cls(self):
        return django_apps.get_model('bhp_personnel.keyperformancearea')
