from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .contract_model_wrapper_mixin import ContractModelWrapperMixin


class ConsultantModelWrapper(ContractModelWrapperMixin, ModelWrapper):

    model = 'bhp_personnel.consultant'
    querystring_attrs = ['identifier']
    next_url_attrs = ['identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('consultant_listboard_url')

    def owner(self):
        employee_cls = django_apps.get_model('bhp_personnel.employee')
        consultant_cls = django_apps.get_model('bhp_personnel.consultant')
        pi_cls = django_apps.get_model('bhp_personnel.pi')
        try:
            employee = employee_cls.objects.get(identifier=object.identifier)
        except employee_cls.DoesNotExist:
            pass
        else:
            return f'{employee.first_name} {employee.middle_name} {employee.last_name}'
        try:
            consultant = consultant_cls.objects.get(identifier=object.identifier)
        except consultant_cls.DoesNotExist:
            pass
        else:
            return f'{consultant.first_name} {consultant.middle_name} {consultant.last_name}'
        try:
            pi = pi_cls.objects.get(identifier=object.identifier)
        except pi_cls.DoesNotExist:
            pass
        else:
            return f'{pi.first_name} {pi.middle_name} {pi.last_name}'
