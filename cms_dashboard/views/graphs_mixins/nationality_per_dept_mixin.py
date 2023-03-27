
from django.apps import apps as django_apps
from edc_base.view_mixins import EdcBaseViewMixin
from bhp_personnel.models import Employee, Department, Contract,Contracting
import re
from django.utils.translation import gettext_lazy as _


class NationalityMixin(EdcBaseViewMixin):
    
    # get the departments
    
    @property
    def dept_name_list(self):
        dept_list = []
        for dept in Department.objects.all():
            dept_list.append(dept.dept_name)
        return dept_list    
        
    
    # count the citizen vs non-citizens
    def get_nationality_count(self):
        citizens =  Employee.objects.filter(nationality='Yes').values_list('identifier').distinct().count()
        non_citizens = Employee.objects.filter(nationality='No').values_list('identifier').distinct().count()
        
        nationality_statistics = [citizens, non_citizens]
        return nationality_statistics
    
    # count citizens vs non citizens per dept
    @property
    def dept_citizen_count(self):
        dept_citizen_count = []
        for dept_name in self.dept_name_list:

            dept_citizen_count.append([dept_name, self.get_dept_nationality_citizens_count(dept_name=dept_name)])   
                   
        return dept_citizen_count    
    
    @property
    def dept_noncitizen_count(self):
        dept_noncitizen_count = []
        for dept_name in self.dept_name_list:
           
            dept_noncitizen_count.append([dept_name ,self.get_dept_nationality_noncitizens_count(dept_name=dept_name)])
        return dept_noncitizen_count    
    
    
    def get_dept_nationality_citizens_count(self,dept_name):
        dept_citizen_obj = Department.objects.filter(dept_name=dept_name)
        count = dept_citizen_obj.first().employee_set.filter(nationality='Yes').values_list('identifier').distinct().count()
        
        return count
    
    def get_dept_nationality_noncitizens_count(self,dept_name):
        dep_noncitizen_obj = Department.objects.filter(dept_name=dept_name)
        count = dep_noncitizen_obj.first().employee_set.filter(nationality='No').values_list('identifier').distinct().count()
        return count
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
    
        context.update(
            nationality_stats = self.get_nationality_count(),
            dept_citizen_stats = self.dept_citizen_count,
            dept_noncitizen_stats = self.dept_noncitizen_count,
            
        )
    
        return context
    
   
