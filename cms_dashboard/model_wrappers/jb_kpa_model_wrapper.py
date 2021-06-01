from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper


class JbDescKpaModelWrapper(ModelWrapper):

    model = 'bhp_personnel.jobdescriptionkpa'
    querystring_attrs = ['key_performance_area']
    next_url_attrs = ['key_performance_area', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def key_performance_area(self):
        return self.object.key_performance_area

    @property
    def job_desc_kpa_cls(self):
        return django_apps.get_model(
            'bhp_personnel.jobdescriptionkpa')
