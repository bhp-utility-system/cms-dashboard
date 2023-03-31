import re

from django.apps import apps as django_apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from edc_base import get_utcnow
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ...model_wrappers import AppraisalModelWrapper, PerformanceImpModelWrapper, \
    RenewalIntentModelWrapper


class AppraisalListBoardView(
    NavbarViewMixin, EdcBaseViewMixin, ListboardFilterViewMixin,
    SearchFormViewMixin, ListboardView):
    listboard_template = 'appraisal_listboard_template'
    listboard_url = 'appraisal_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"

    model = 'bhp_personnel.performanceassessment'
    model_wrapper_cls = AppraisalModelWrapper
    navbar_name = 'cms_main_dashboard'
    navbar_selected_item = None
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'appraisal_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @property
    def performance_imp_obj(self):
        """Returns a non persistent obj
        """
        performance_imp_cls = django_apps.get_model('bhp_personnel.performanceimpplan')
        pio = None
        try:
            performance_imp = performance_imp_cls.objects.get(
                contract=self.contract_obj)
        except performance_imp_cls.DoesNotExist:
            pio = performance_imp_cls(contract=self.contract_obj,
                                      emp_identifier=self.contract_obj.identifier)
        else:
            pio = performance_imp
        finally:
            return PerformanceImpModelWrapper(pio)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract = self.kwargs.get('contract')
        model_cls = django_apps.get_model('bhp_personnel.performanceassessment')
        wrapped = self.model_wrapper_cls(
            model_cls(contract=self.contract_obj,
                      emp_identifier=self.contract_obj.identifier))

        context.update(
            contract=contract,
            employee_obj=self.employee,
            contract_obj=self.contract_obj,
            contract_due=self.is_contract_due,
            renewal_intent=self.get_renewal_intent,
            appraisal_add_url=wrapped.href,
            performance_imp_obj=self.performance_imp_obj,
            renewal_intent_wrapped_obj=self.renewal_intent_wrapped_obj,
        )
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('identifier'):
            options.update(
                {'identifier': kwargs.get('identifier')})
        if kwargs.get('contract'):
            options.update(
                {'contract': kwargs.get('contract')})
        options.update()
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            intent = self.request.POST.get('intent')
            renewal_intent_cls = django_apps.get_model('bhp_personnel.renewalintent')
            employee_obj = self.employee

            if employee_obj.email == self.request.user.email and\
                    self.get_renewal_intent is None:
                renewal_intent_cls.objects.create(
                    contract=self.contract_obj,
                    intent=intent
                )
                messages.success(request, 'Your renewal intent has been successfully submitted.')

            elif self.get_renewal_intent and employee_obj.supervisor.email == self.request.user.email:
                comment = request.POST.get('comment')

                if comment:
                    self.update_intent(identifier=self.contract_obj.identifier, comment=comment,
                                       request=request)
        return HttpResponseRedirect(self.request.path)

    def update_intent(self, identifier=None, comment=None, request=None):
        renewal_intent_obj = self.latest_renewal_intent_obj(identifier)
        renewal_intent_obj.comment = comment
        renewal_intent_obj.save()
        messages.success(request, 'Comment successfully saved')

    def latest_renewal_intent_obj(self, identifier=None):
        try:
            renewal_intent_obj = self.renewal_intent_cls.objects.filter(
                contract__identifier=identifier,
            ).earliest('contract__start_date')
        except self.renewal_intent_cls.DoesNotExist:
            return None
        else:
            return renewal_intent_obj

    @property
    def contract_obj(self):
        contract_model_cls = django_apps.get_model('bhp_personnel.contract')
        try:
            contract = contract_model_cls.objects.get(
                id=self.kwargs.get('contract'))
        except contract_model_cls.DoesNotExist:
            raise ValidationError('Please make sure this contract exists.')
        else:
            return contract

    @property
    def is_contract_due(self):
        return self.contract_obj.due_date < get_utcnow().date()

    @property
    def get_renewal_intent(self):
        if hasattr(self.contract_obj, 'renewalintent'):
            return self.contract_obj.renewalintent
        else:
            return None
    @property
    def employee(self):
        """Return an employee.
        """
        identifier = self.contract_obj.identifier
        try:
            employee = django_apps.get_model('bhp_personnel.employee').objects.get(
                identifier=identifier)
        except django_apps.get_model('bhp_personnel.employee').DoesNotExist:
            raise ValidationError(
                f"Employee with identifier {identifier} does not exist")
        else:
            return employee

    @property
    def renewal_intent_cls(self):
        return django_apps.get_model('bhp_personnel.renewalintent')

    @property
    def renewal_intent_wrapped_obj(self):
        model_obj = self.renewal_intent_cls(
            contract=self.contract_obj,
        )
        return RenewalIntentModelWrapper(model_obj=model_obj)