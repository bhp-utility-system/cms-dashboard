from .professional_skills_model_wrapper import (
    StrategicOrientationModelWrapper, ResultsFocusModelWrapper,
    LeadershipAndMotivationModelWrapper, InnovationAndCreativityModelWrapper,
    PlanningSkillsModelWrapper, InterpersonalSkillsModelWrapper,
    CommunicationSkillsModelWrapper, KnowledgeAndProductivityModelWrapper,
    QualityOfWorkModelWrapper)
from .model_wrapper_mixin import ProfessionalSkillsWrapperMixin


class StrategicOrientationModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    strategic_model_cls = 'bhp_personnel.strategicorientation'
    strategic_wrapper_cls = StrategicOrientationModelWrapper

    def strategic_model_obj(self):
        return super().model_obj(self.strategic_model_cls)


class ResultsFocusModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    results_focus_model_cls = 'bhp_personnel.resultsfocus'
    results_focus_wrapper_cls = ResultsFocusModelWrapper

    def results_focus_obj(self):
        return super().model_obj(self.results_focus_model_cls)


class LeadershipAndMotivationModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    leadership_model_cls = 'bhp_personnel.leadershipandmotivation'
    leadership_wrapper_cls = LeadershipAndMotivationModelWrapper

    def leadership_and_motivation_obj(self):
        return super().model_obj(self.leadership_model_cls)


class InnovationAndCreativityModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    innovation_model_cls = 'bhp_personnel.innovationandcreativity'
    innovation_wrapper_cls = InnovationAndCreativityModelWrapper

    def innovation_obj(self):
        return super().model_obj(self.innovation_model_cls)


class PlanningSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    planning_skills_model_cls = 'bhp_personnel.planningskills'
    planning_skills_wrapper_cls = PlanningSkillsModelWrapper

    def planning_skills_obj(self):
        return super().model_obj(self.planning_skills_model_cls)


class InterpersonalSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    interpersonal_skills_model_cls = 'bhp_personnel.interpersonalskills'
    interpersonal_skills_wrapper_cls = InterpersonalSkillsModelWrapper

    def interpersonal_obj(self):
        return super().model_obj(self.interpersonal_skills_model_cls)


class CommunicationSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    communication_skills_model_cls = 'bhp_personnel.communicationskills'
    communication_skills_wrapper_cls = CommunicationSkillsModelWrapper

    def communication_obj(self):
        return super().model_obj(self.communication_skills_model_cls)


class KnowledgeAndProductivityModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    knowledge_model_cls = 'bhp_personnel.knowledgeandproductivity'
    knowledge_wrapper_cls = KnowledgeAndProductivityModelWrapper

    def knowledge_obj(self):
        return super().model_obj(self.knowledge_model_cls)


class QualityOfWorkModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    quality_of_work_model_cls = 'bhp_personnel.qualityofwork'
    quality_of_work_wrapper_cls = QualityOfWorkModelWrapper

    def quality_model_obj(self):
        return super().model_obj(self.quality_of_work_model_cls)
