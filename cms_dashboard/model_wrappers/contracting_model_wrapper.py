from django.conf import settings
from edc_model_wrapper import ModelWrapper


class ContractingModelWrapper(ModelWrapper):

    model = 'bhp_personnel.contracting'
    querystring_attrs = ['contract', 'identifier', 'supervisor',
                         'department']
    next_url_attrs = ['identifier', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('employee_dashboard_url')

    @property
    def identifier(self):
        return self.object.identifier 

    @property
    def supervisor(self):
        return self.object.supervisor

    @property
    def department(self):
        return self.object.department
