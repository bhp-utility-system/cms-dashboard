
from curses import ungetmouse
from django.apps import apps as django_apps
from edc_base.view_mixins import EdcBaseViewMixin
from datetime import datetime
import statistics
import numpy as np
from django.core.exceptions import ObjectDoesNotExist

class AgeDistributionPerStudyMixin(EdcBaseViewMixin):
    
    study_age_outliers = []
    
    @property
    def studies_model_cls(self):
        return django_apps.get_model('bhp_personnel.studies')
    
    @property
    def study_name_list(self):
        study_name_list = []
        
        for study in self.studies_model_cls.objects.all():
            study_name_list.append(study.name)
        
        return study_name_list    
    
    @property
    def age_distribution_per_study(self):
        employee_age_dist = []
        
        for study in self.study_name_list:
            try:
                obj = self.get_employee_ages_per_study(study_name=study)
            except ValueError:
                pass
            else:
                if len(obj) > 0:
                    employee_age_dist.append([study, obj])
                         
        return employee_age_dist
    
    # calculate age
    def age(self,dob=None):
        df = datetime.now().date() 
        #  age = enrolment_date.year - dob.year - ((enrolment_date.month, enrolment_date.day) < (dob.month, dob.day))
        # age_in_years = df.year - dob.year ((df.month, df.day) < (dob.month, dob.day))
        age_in_years = df.year - dob.year -((df.month, df.day) < (dob.month, dob.day))
        return age_in_years
    
    
    def get_employee_ages_per_study(self, study_name):
        study_employee_age_obj =  self.studies_model_cls.objects.filter(name=study_name)
        formatted_age_in_years_list = []
        
        # create a try except
        try:
            obj = study_employee_age_obj.first().employee_set.all()
        except ObjectDoesNotExist: 
            return None                
        else:
            if obj.count() > 0:
                employee_ages_list = study_employee_age_obj.first().employee_set.all().values_list('date_of_birth')
                for age in employee_ages_list:              
                    formatted_age_in_years_list.append(self.age(age[0]))
                      


        # if study_employee_age_obj.first().employee_set.all():
        #     employee_ages_list = study_employee_age_obj.first().employee_set.all().values_list('date_of_birth')
        #     for age in employee_ages_list:
        #         formatted_age_in_years_list.append(self.age(age[0]))
            
        # else:
        #     employee_ages_list = None
           
            median = statistics.median(formatted_age_in_years_list)    
            upperquartile = np.quantile(formatted_age_in_years_list, .75) 
            lowerquartile = np.quantile(formatted_age_in_years_list, .25)  
            IQR = upperquartile - lowerquartile
            max_whisker =  upperquartile+(1.5 * IQR) 
            min_whisker =  lowerquartile-(1.5 * IQR)
            
            min_outlier_ages = []
            max_outlier_ages = []
            
            for age in formatted_age_in_years_list:
                if age < max_whisker:
                    min_outlier_ages.append(age)
                else:
                    self.study_age_outliers.append([study_name,age])    
                if age > min_whisker:
                    max_outlier_ages.append(age)
                else:
                    self.study_age_outliers.append([study_name,age])    
            
            min = np.min(max_outlier_ages)   
            max = np.max(min_outlier_ages)     
            
        return [min,lowerquartile,median,upperquartile,max]   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update(
            
            age_dist = self.age_distribution_per_study,
            study_age_outliers = self.study_age_outliers,
        )
        return context