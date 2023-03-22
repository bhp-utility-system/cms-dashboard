from django.conf import settings
from edc_model_wrapper import ModelWrapper


class RenewalIntentModelWrapper(ModelWrapper):
    model = 'bhp_personnel.renewalintent'
    querystring_attrs = ['contract']
    next_url_attrs = ['contract']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract