from django.apps import apps as django_apps
from django.conf import settings

from edc_model_wrapper import ModelWrapper

from .employee_model_wrapper_mixin import EmployeeModelWrapperMixin
from .kpa_model_wrapper_mixin import KpaModelWrapperMixin
from .kpa_model_wrapper import KpaModelWrapper
from .professional_skills_model_wrapper_mixin import (
    StrategicOrientationModelWrapperMixin, ResultsFocusModelWrapperMixin,
    LeadershipAndMotivationModelWrapperMixin,
    InnovationAndCreativityModelWrapperMixin, PlanningSkillsModelWrapperMixin,
    InterpersonalSkillsModelWrapperMixin, CommunicationSkillsModelWrapperMixin,
    KnowledgeAndProductivityModelWrapperMixin, QualityOfWorkModelWrapperMixin)
from .performance_imp_model_wrapper_mixin import \
    PerformanceImpModelWrapperMixin


class AppraisalModelWrapper(EmployeeModelWrapperMixin,
                            PerformanceImpModelWrapperMixin,
                            KpaModelWrapperMixin,
                            QualityOfWorkModelWrapperMixin,
                            KnowledgeAndProductivityModelWrapperMixin,
                            CommunicationSkillsModelWrapperMixin,
                            InterpersonalSkillsModelWrapperMixin,
                            PlanningSkillsModelWrapperMixin,
                            InnovationAndCreativityModelWrapperMixin,
                            LeadershipAndMotivationModelWrapperMixin,
                            ResultsFocusModelWrapperMixin,
                            StrategicOrientationModelWrapperMixin,
                            ModelWrapper):

    model = 'bhp_personnel.performanceassessment'
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

    # @property
    # def kpa_cls(self):
    #     return django_apps.get_model(
    #         'bhp_personnel.keyperformancearea')

    @property
    def kpa_cls(self):
        return django_apps.get_model('bhp_personnel.keyperformancearea')

    @property
    def kpa_list(self):
        wrapped_kpas = []
        kpas = self.kpa_cls.objects.filter(contract=self.contract,
                                           assessment_period_type=self.object.review)
        for kpa in kpas:
            wrapped_kpas.append(KpaModelWrapper(kpa))
        return wrapped_kpas

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
        if self.contract:
            total = 0

            total += self.get_professional_skills_scores()

            if total > 0:
                total *= 0.8

            key_performance_cls = django_apps.get_model('bhp_personnel.keyperformancearea')

            key_performance_objs = key_performance_cls.objects.filter(
                    contract=self.contract,
                    assessment_period_type=self.object.review)

            total_performance_score = 0
            for obj in key_performance_objs:
                if obj.kpa_score:
                    total_performance_score += float(obj.kpa_score)

            if total_performance_score > 0:
                total += ((total_performance_score / key_performance_objs.count()) * 0.2)
            return round(total, 2)
