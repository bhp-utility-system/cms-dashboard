from django.apps import apps as django_apps
from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .kpa_model_wrapper import KpaModelWrapper
from .kpa_model_wrapper_mixin import KpaModelWrapperMixin
from .performance_imp_model_wrapper_mixin import \
    PerformanceImpModelWrapperMixin


class AppraisalModelWrapper(EmployeeModelWrapperMixin,
                            KpaModelWrapperMixin,
                            ModelWrapper):

    model = 'bhp_personnel.appraisal'
    querystring_attrs = ['contract', 'emp_identifier', ]
    next_url_attrs = ['contract', 'emp_identifier', ]
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract

    @property
    def emp_identifier(self):
        return self.object.emp_identifier

    @property
    def contract_cls(self):
        return django_apps.get_model('bhp_personnel.contract')

    @property
    def performance_review_cls(self):
        return django_apps.get_model('bhp_personnel.performancereview')

    @property
    def performance_review_list(self):
        performance_review = self.performance_review_cls.objects.filter(appraisal=self.object)
        return performance_review

    def get_professional_skills_scores(self):
        models = ['strategicorientation', 'resultsfocus',
                  'leadershipandmotivation', 'innovationandcreativity',
                  'planningskills', 'interpersonalskills',
                  'communicationskills', 'knowledgeandproductivity',
                  'qualityofwork', ]

        fields = ['strategic_orientation', 'results_focus',
                  'leadership_motivation', 'innovation_creativity',
                  'planning_skills', 'interpersonal_skills',
                  'communication_skills', 'productivity',
                  'quality_of_work', ]
        score = 0
        count = 0
        for field, model in zip(fields, models):
            model_cls = django_apps.get_model(f'bhp_personnel.{model}')

            try:
                model_obj = model_cls.objects.get(contract=self.contract,
                                                  assessment_period_type=self.object.review)
            except model_cls.DoesNotExist:
                pass
            else:
                count += 1
                score += int(getattr(model_obj, field))
        if score > 0 and count > 0:
            score /= count
        return score

    @property
    def overall_score(self):
        if self.performance_review_list:
            total = 0
            for kpa in self.performance_review_list:
                total += kpa.review_score
            if total > 0:
                total = total / len(self.performance_review_list)
            return round(total, 1)
        return None
