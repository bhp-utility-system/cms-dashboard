import re
from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ..contract_filters import ContractListBoardFilters
from ...model_wrappers import ContractModelWrapper


class ContractListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                            ListboardFilterViewMixin, SearchFormViewMixin,
                            ListboardView):

    listboard_template = 'contract_listboard_template'
    listboard_url = 'contract_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"

    listboard_view_filters = ContractListBoardFilters()
    model = 'bhp_personnel.contract'
    model_wrapper_cls = ContractModelWrapper
    navbar_name = 'cms_dashboard'
    navbar_selected_item = 'contract'
    ordering = '-modified'
    paginate_by = 10
    search_form_url = 'contract_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            personnel_name=self.model_wrapper_cls.personnel_name,
            contract_add_url=self.model_cls().get_absolute_url()
            )
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        usr_groups = [g.name for g in self.request.user.groups.all()]

        if kwargs.get('identifier'):
            options.update(
                {'identifier': kwargs.get('identifier')})
        if 'Supervisor' in usr_groups or request.GET.get('p_role') == 'Supervisor':
            employee_cls = django_apps.get_model('bhp_personnel.employee')
            employee_ids = employee_cls.objects.filter(
                supervisor__email=self.request.user.email).values_list('identifier', flat=True)
            if not employee_ids:
                options.update({'user_created': None})
            else:
                options.update({'identifier__in': employee_ids})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
