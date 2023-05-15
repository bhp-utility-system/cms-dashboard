from django.conf import settings
from edc_model_wrapper import ModelWrapper
from django.apps import apps as django_apps


class ContractingModelWrapper(ModelWrapper):
    model = 'bhp_personnel.contracting'
    querystring_attrs = ['contract', 'identifier', 'supervisor',
                         'department']
    next_url_attrs = ['identifier', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_dashboard_url')

    employee_model_cls = 'bhp_personnel.employee'
    contract_model_cls = 'bhp_personnel.contract'

    @property
    def identifier(self):
        return self.object.identifier

    @property
    def supervisor(self):
        employee = self.employee_model_obj
        return employee.supervisor

    @property
    def department(self):
        return self.object.department

    @property
    def employee_model_obj(self):
        try:
            obj = self.employee_model_cls.objects.get(identity=self.identifier)
        except self.employee_model_cls.DoesNotExist:
            raise
        else:
            return obj

    @property
    def contract(self):
        if self.object:
            return self.object.contract
