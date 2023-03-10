from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user
from edc_base.utils import get_utcnow
from dateutil.relativedelta import relativedelta
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from bhp_personnel.models import Contract, Consultant, Employee, Pi


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):
    template_name = 'cms_dashboard/home.html'
    navbar_name = 'cms_main_dashboard'
    navbar_selected_item = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Employee.objects.all()
        consultant = Consultant.objects.all()
        contracts = Contract.objects.all()
        pi = Pi.objects.all()

        total = employees.count() + consultant.count() + pi.count()

        employee_contracts = Contract.objects.filter(
            identifier__startswith="E")
        pi_contracts = Contract.objects.filter(
            identifier__startswith="P")
        consultant_contracts = Contract.objects.filter(
            identifier__startswith="C")

        active_employees = Contract.objects.filter(
            identifier__startswith="E", status="Active")
        active_pis = Contract.objects.filter(
            identifier__startswith="P", status="Active")
        active_consultants = Contract.objects.filter(
            identifier__startswith="C", status="Active")

        active_contracts = active_employees.count() + \
                           active_pis.count() + active_consultants.count()

        employee_completed = Contract.objects.filter(
            identifier__startswith="E", contract_ended="True")
        pi_completed = Contract.objects.filter(
            identifier__startswith="P", contract_ended="True")
        consultant_completed = Contract.objects.filter(
            identifier__startswith="C", contract_ended="True")

        completed_contracts = employee_completed.count() + \
                              pi_completed.count() + consultant_completed.count()

        current_user = get_user(self.request)
        employee_supervisees = Employee.objects.filter(
            supervisor__email=current_user.email)
        consultant_supervisees = Consultant.objects.filter(
            supervisor__email=current_user.email)
        pi_supervisees = Pi.objects.filter(
            supervisor__email=current_user.email)

        three_months_ahead = get_utcnow().date() + relativedelta(months=3)

        due_contracts = Contract.objects.filter(
            end_date__range=[get_utcnow().date(), three_months_ahead],
        )

        context.update(
            total=total,
            employees_total=employees.count(),
            consultant_total=consultant.count(),
            pi_total=pi.count(),

            employee_contracts=employee_contracts.count(),
            pi_contracts=pi_contracts.count(),
            consultant_contracts=consultant_contracts.count(),
            all_contracts=Contract.objects.all().count(),

            # Active Contracts
            active_employees=active_employees.count(),
            active_pis=active_pis.count(),
            active_consultants=active_consultants.count(),
            active_contracts=active_contracts,
            due_contracts=due_contracts.count(),

            # Complete Contracts
            employee_completed=employee_completed.count(),
            pi_completed=pi_completed.count(),
            consultant_completed=consultant_completed.count(),
            completed_contracts=completed_contracts,

            # Supervisees
            employee_supervisees=employee_supervisees.count(),
            consultant_supervisees=consultant_supervisees.count(),
            pi_supervisees=pi_supervisees.count(),

            employee_identifier=self.employee_logged_in.identifier,
            is_supervisor=self.is_supervisor
        )
        return context

    @property
    def employee_logged_in(self):
        current_user = get_user(self.request)
        try:
            employee = Employee.objects.get(email=current_user.email)
        except Employee.DoesNotExist:
            raise ValidationError('Employee with email, does not exist.')
        else:
            return employee

    @property
    def is_supervisor(self):
        supervisor_cls = django_apps.get_model('bhp_personnel.supervisor')
        current_user = get_user(self.request)
        try:
            supervisor_cls.objects.get(email=current_user.email)
        except supervisor_cls.DoesNotExist:
            return False
        else:
            return True
