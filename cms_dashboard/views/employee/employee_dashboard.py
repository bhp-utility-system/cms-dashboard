from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from bhp_personnel.models import Contract, Employee
from ...model_wrappers import ContractModelWrapper


class DashboardView(NavbarViewMixin, EdcBaseViewMixin, TemplateView):

    template_name = 'cms_dashboard/employee/employee_dashboard.html'
    navbar_name = 'cms_main_dashboard'

    @property
    def job_description_model_cls(self):
        return django_apps.get_model('bhp_personnel.jobdescription')

    def contracts(self, identifier=None):
        """Returns a Queryset of all contracts for this subject.
        """
        wrapped_objs = []
        for contract in Contract.objects.filter(identifier=identifier):
            wrapped_objs.append(ContractModelWrapper(contract))

        return wrapped_objs

    def contract(self, identifier=None):
        """Reeturn a new contract obj.
        """
        job_description = None
        job_descriptions = self.job_description_model_cls.objects.filter(
            identifier=identifier).order_by('-created')
        if job_descriptions:
            job_description = job_descriptions.first()
        return ContractModelWrapper(
            Contract(job_description=job_description, identifier=identifier))

    def employee(self, identifier=None):
        """Return an employee.
        """
        try:
            employee = Employee.objects.get(identifier=identifier)
        except Employee.DoesNotExist:
            raise ValidationError(
                f"Employee with identifier {identifier} does not exist")
        else:
            return employee

    def any_active_contract(self, identifier):
        """Return true if there is any active contract for employee"""
        contracts = Contract.objects.filter(identifier=identifier, status='Active')
        return True if contracts else False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        identifier = kwargs.get('identifier', None)
        context.update(
            identifier=identifier,
            employee=self.employee(identifier=identifier),
            contracts=self.contracts(identifier=identifier),
            contract=self.contract(identifier=identifier),
            active_contract=self.any_active_contract(identifier),
            employee_contracts=Contract.objects.filter(identifier=identifier).count())
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
