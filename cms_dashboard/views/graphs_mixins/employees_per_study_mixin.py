from django.apps import apps as django_apps
from edc_base.view_mixins import EdcBaseViewMixin


class EmployeesPerStudyMixin(EdcBaseViewMixin):

    @property
    def studies_model_cls(self):
        return django_apps.get_model('bhp_personnel.studies')

    @property
    def study_names_list(self):
        study_names_list = []

        for study in self.studies_model_cls.objects.all():
            study_names_list.append(study.name)
        return study_names_list

    @property
    def employees_per_study(self):

        study_statistics = []

        for study in self.study_names_list:
            study_statistics.append([study, self.get_study_employee(study_name=study)])
        return study_statistics

    def get_study_employee(self, study_name):

        study_obj = self.studies_model_cls.objects.filter(name=study_name)

        if study_obj.first().employee_set.all():
            employee_list = study_obj.first().employee_set.all()
        else:
            employee_list = []
        return employee_list

    def get_study_employee_count(self, study_name):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            study_names_list=self.study_names_list,
            employees_per_study=self.employees_per_study
        )
        return context
