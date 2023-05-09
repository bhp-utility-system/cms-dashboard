from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from bhp_personnel.models import Employee


class EmployeeUpdateView(NavbarViewMixin, EdcBaseViewMixin, UpdateView):
    model = Employee
    template_name = 'cms_dashboard/employee/dashboard/edit_personal_details.html'
    success_url = reverse_lazy('cms_dashboard:update_employee_info_url')
    fields = ['title_salutation', 'country', 'postal_address', 'physical_address',
              'cell', 'email', 'highest_qualification', 'next_of_kin_contact']
    navbar_name = 'cms_main_dashboard'

    def get_object(self, queryset=None):
        identifier = self.kwargs.get('slug')
        employee = get_object_or_404(Employee, identifier=identifier)
        return employee

    def get_success_url(self):
        identifier = self.kwargs.get('slug')
        return reverse_lazy('cms_dashboard:employee_dashboard_url',
                            kwargs={'identifier': identifier})

    def form_valid(self, form):
        messages.success(self.request, 'Your information has been updated!')
        return super().form_valid(form)
