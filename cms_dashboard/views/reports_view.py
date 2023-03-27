from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from .graphs_mixins import (GenderGraphMixin, EmployeePerDeptGraphMixin,
                            NationalityMixin, EmployeesPerStudyMixin,
                            AgeDistributionPerStudyMixin, EmployeeContractMixin)


class ReportsView(AgeDistributionPerStudyMixin, EmployeeContractMixin, EmployeesPerStudyMixin,
                  NationalityMixin, EmployeePerDeptGraphMixin, GenderGraphMixin,
                  NavbarViewMixin, EdcBaseViewMixin, TemplateView):
    template_name = 'cms_dashboard/reports.html'
    navbar_selected_item = 'reports'
    navbar_name = 'cms_dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
