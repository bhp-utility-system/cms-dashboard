from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .consultant_model_wrapper_mixin import ConsultantModelWrapperMixin
from .pi_model_wrapper_mixin import PiModelWrapperMixin
from .contracting_model_wrapper_mixin import ContractingModelWrapperMixin


class RenewalIntentModelWrapper(EmployeeModelWrapperMixin, ConsultantModelWrapperMixin,
                           ContractingModelWrapperMixin, PiModelWrapperMixin,
                           ModelWrapper):

    model = 'bhp_personnel.renewalintent'
    querystring_attrs = ['contract', ]
    next_url_attrs = ['contract', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')


    @property
    def contract(self):
        return self.object.contract
