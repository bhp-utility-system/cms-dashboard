from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_dashboard.listboard_filter import ListboardFilter, \
    ListboardViewFilters


class ListBoardFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        label='All',
        lookup={})

    active = ListboardFilter(
        label='Active',
        position=10,
        lookup={'status': 'Active',
                'contract_ended': False})

    not_active = ListboardFilter(
        label='Not Active',
        position=10,
        lookup={'status': 'Not Active'})

    completed = ListboardFilter(
        label='Completed',
        position=11,
        lookup={'contract_ended': True})

    incomplete = ListboardFilter(
        label='In Progress',
        position=11,
        lookup={'contract_ended': False})

    due_date = ListboardFilter(
        label='3-Months Due',
        position=12,
        lookup={'end_date__range': [get_utcnow().date(), get_utcnow().date() + relativedelta(months=3)]})


class EmployeeListBoardFilters(ListboardViewFilters):
    
        all = ListboardFilter(
        name='all',
        label='All',
        lookup={})
        
        gender_female = ListboardFilter(
            name ='gender_female',
            label = 'Female',
            lookup = {'gender': 'F'}
        )
        
        gender_male = ListboardFilter(
            name ='gender_male',
            label = 'Male',
            lookup = {'gender': 'M'}
        )