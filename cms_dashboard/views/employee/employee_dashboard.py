from django.apps import apps as django_apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import YES
from edc_navbar import NavbarViewMixin

from ...model_wrappers import ContractModelWrapper


class DashboardView(NavbarViewMixin, EdcBaseViewMixin, TemplateView):

    template_name = 'cms_dashboard/employee/employee_dashboard.html'
    navbar_name = 'cms_main_dashboard'
    contracting_model = 'bhp_personnel.contracting'
    contract_model = 'bhp_personnel.contract'
    identifier = ''

    @property
    def contracting_model_cls(self):
        return django_apps.get_model(self.contracting_model)

    @property
    def contract_model_cls(self):
        return django_apps.get_model(self.contract_model)

    @property
    def employee_model_cls(self):
        return django_apps.get_model('bhp_personnel.employee')

    @property
    def renewal_intent_cls(self):
        return django_apps.get_model('bhp_personnel.renewalintent')

    def contracts(self, identifier=None):
        """Returns a Queryset of all contracts for this subject.
        """
        wrapped_objs = []
        for contract in self.contract_model_cls.objects.filter(identifier=identifier):
            wrapped_objs.append(ContractModelWrapper(contract))

        return wrapped_objs

    def contract(self, identifier=None):
        """Return a new contract obj.
        """
        contract = self.contract_model_cls(identifier=identifier)
        return ContractModelWrapper(contract)

    def employee(self, identifier=None):
        """Return an employee.
        """
        try:
            employee = self.employee_model_cls.objects.get(identifier=identifier)
        except self.employee_model_cls.DoesNotExist:
            raise ValidationError(
                f"Employee with identifier {identifier} does not exist")
        else:
            return employee

    def any_active_contract(self, identifier):
        """Return true if there is any active contract for employee"""
        contracts = self.contract_model_cls.objects.filter(
            identifier=identifier, status='Active')
        return True if contracts else False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.identifier = kwargs.get('identifier', None)
        context.update(
            YES=YES,
            identifier=self.identifier,
            renewal_intent=self.latest_renewal_intent_obj(identifier=self.identifier),
            employee=self.employee(identifier=self.identifier),
            contracts=self.contracts(identifier=self.identifier),
            contract=self.contract(identifier=self.identifier),
            active_contract=self.any_active_contract(self.identifier),
            employee_contracts=self.contract_model_cls.objects.filter(
                identifier=self.identifier).count())
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
