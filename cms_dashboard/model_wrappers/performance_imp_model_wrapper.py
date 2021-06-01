from django.conf import settings

from edc_model_wrapper import ModelWrapper


class PerformanceImpModelWrapper(ModelWrapper):

    model = 'bhp_personnel.performanceimpplan'
    querystring_attrs = ['contract', 'emp_identifier']
    next_url_attrs = ['contract', 'emp_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract
