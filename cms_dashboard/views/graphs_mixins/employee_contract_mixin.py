from dateutil.relativedelta import relativedelta
from django.apps import apps as django_apps
from django.db.models import Count
from edc_base.view_mixins import EdcBaseViewMixin
from edc_utils import get_utcnow

from bhp_personnel.models import Employee


class EmployeeContractMixin(EdcBaseViewMixin):

    @property
    def contract_model_cls(self):
        return django_apps.get_model('bhp_personnel.contract')

    @property
    def get_contract_employee_list(self):
        contracts = self.contract_model_cls.objects.all()
        contract_employee_list = []
        for contract in contracts:
            employee = Employee.objects.filter(identifier=contract.identifier).first()
            contract_employee_list.append({'employee': employee, 'contract': contract})
        return contract_employee_list

    @property
    def get_due_contracts(self):
        """
        get contracts ending in 3 months from now
        """
        three_months_ahead = get_utcnow().date() + relativedelta(months=3)

        due_contracts = self.contract_model_cls.objects.filter(
            end_date__range=[get_utcnow().date(), three_months_ahead],
        )

        return due_contracts

    @property
    def get_due_contracts_by_department(self):
        """
        group contracts by department 
        """
        due_contracts = self.get_due_contracts
        due_contract_per_department = (
            Employee.objects
            .filter(identifier__in=[contract.identifier for contract in due_contracts])
            .values('department__dept_name')
            .annotate(count=Count('identifier'))
        )
        return due_contract_per_department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            contracts=self.get_contract_employee_list,
            due_contracts=self.get_due_contracts,
            due_contracts_per_department=self.get_due_contracts_by_department
        )
        return context
