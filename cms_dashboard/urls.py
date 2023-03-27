"""potlako_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/"""
from django.urls import path

from edc_dashboard import UrlConfig

from .patterns import contract, identifier
from .views import (
    ContractListBoardView, ConsultantListBoardView, EmployeeListBoardView,
    PiListBoardView, DashboardView, PiDashboardView, ConsultantDashboardView,
    HomeView, AppraisalListBoardView, ReportsView)
from .views.contract import (
    ConsultantContractListBoardView, EmployeeContractListboardView,
    PiContractListBoardView)

app_name = 'cms_dashboard'

appraisal_listboard_url_config = UrlConfig(
    url_name='appraisal_listboard_url',
    view_class=AppraisalListBoardView,
    label='appraisal_listboard',
    identifier_label='contract',
    identifier_pattern=contract)

contract_listboard_url_config = UrlConfig(
    url_name='contract_listboard_url',
    view_class=ContractListBoardView,
    label='contract_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

empcontract_listboard_url_config = UrlConfig(
    url_name='emp_contract_listboard_url',
    view_class=EmployeeContractListboardView,
    label='employee_contracts_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

consultant_dashboard_url_config = UrlConfig(
    url_name='consultant_dashboard_url',
    view_class=ConsultantDashboardView,
    label='consultant_dashboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

consultant_listboard_url_config = UrlConfig(
    url_name='consultant_listboard_url',
    view_class=ConsultantListBoardView,
    label='consultant_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

consultant_contract_listboard_url_config = UrlConfig(
    url_name='consultant_contract_listboard_url',
    view_class=ConsultantContractListBoardView,
    label='consultant_contracts_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

employee_dashboard_url_config = UrlConfig(
    url_name='employee_dashboard_url',
    view_class=DashboardView,
    label='employee_dashboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

employee_listboard_url_config = UrlConfig(
    url_name='employee_listboard_url',
    view_class=EmployeeListBoardView,
    label='employee_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

pi_listboard_url_config = UrlConfig(
    url_name='pi_listboard_url',
    view_class=PiListBoardView,
    label='pi_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

pi_dashboard_url_config = UrlConfig(
    url_name='pi_dashboard_url',
    view_class=PiDashboardView,
    label='pi_dashboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

pi_contract_dashboard_url_config = UrlConfig(
    url_name='pi_contract_listboard_url',
    view_class=PiContractListBoardView,
    label='pi_contracts_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

urlpatterns = [
    # path('dashboard/<identifier>', DashboardView.as_view(), name='dashboard_url'),
]

urlpatterns += [path('cms/', HomeView.as_view(), name='cms_url')]
urlpatterns += [path('reports/', ReportsView.as_view(), name='reports_url')]
urlpatterns += appraisal_listboard_url_config.listboard_urls
urlpatterns += contract_listboard_url_config.listboard_urls
urlpatterns += consultant_dashboard_url_config.dashboard_urls
urlpatterns += consultant_contract_listboard_url_config.listboard_urls
urlpatterns += consultant_listboard_url_config.listboard_urls
urlpatterns += employee_dashboard_url_config.dashboard_urls
urlpatterns += employee_listboard_url_config.listboard_urls
urlpatterns += empcontract_listboard_url_config.listboard_urls
urlpatterns += pi_dashboard_url_config.dashboard_urls
urlpatterns += pi_listboard_url_config.listboard_urls
urlpatterns += pi_contract_dashboard_url_config.listboard_urls
