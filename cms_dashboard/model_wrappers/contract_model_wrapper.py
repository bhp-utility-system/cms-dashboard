from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .consultant_model_wrapper_mixin import ConsultantModelWrapperMixin
from .pi_model_wrapper_mixin import PiModelWrapperMixin
from .contracting_model_wrapper_mixin import ContractingModelWrapperMixin


class ContractModelWrapper(EmployeeModelWrapperMixin, ConsultantModelWrapperMixin,
                           ContractingModelWrapperMixin, PiModelWrapperMixin,
                           ModelWrapper):

    model = 'bhp_personnel.contract'
    querystring_attrs = ['identifier', 'id']
    next_url_attrs = ['identifier', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_dashboard_url')

    @property
    def personnel_name(self):
        full_name = None

        if self.object.identifier[0] == 'E':
            first_name = self.emp_first_name
            last_name = self.emp_last_name
            if first_name is not None and last_name is not None:
                full_name = first_name + ' ' + last_name

        elif self.object.identifier[0] == 'P':
            first_name = self.pi_first_name
            last_name = self.pi_last_name
            if first_name is not None and last_name is not None:
                full_name = first_name + ' ' + last_name

        elif self.object.identifier[0] == 'C':
            first_name = self.consultant_first_name
            last_name = self.consultant_last_name
            if first_name is not None and last_name is not None:
                full_name = first_name + ' ' + last_name

        return full_name

    @property
    def contract(self):
        return self.object

    @property
    def jd_initials(self):
        initial = {}
        if getattr(self, 'employee_model_obj', None):
            initial['job_title'] = self.employee_model_obj.job_title
            initial['supervisor'] = self.employee_model_obj.supervisor
            initial['department'] = self.employee_model_obj.department
        if getattr(self, 'consultant_model_obj', None):
            pass
        if getattr(self, 'pi_model_obj', None):
            pass
        return initial
