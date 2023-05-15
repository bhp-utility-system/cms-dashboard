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

    @property
    def emp_identifier(self):
        return self.object.contract.identifier

    def create_options(self):
        """Returns a dictionary of options to create a new
        unpersisted model instance.
        """
        options = dict(
            contract=self.object.contract
        )
        return options
