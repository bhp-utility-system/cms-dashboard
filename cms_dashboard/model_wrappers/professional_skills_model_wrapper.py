from .model_wrapper_mixin import ProfessionalSkillsWrapper


class StrategicOrientationModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.strategicorientation'


class ResultsFocusModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.resultsfocus'


class LeadershipAndMotivationModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.leadershipandmotivation'


class InnovationAndCreativityModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.innovationandcreativity'


class PlanningSkillsModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.planningskills'


class InterpersonalSkillsModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.interpersonalskills'


class CommunicationSkillsModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.communicationskills'


class KnowledgeAndProductivityModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.knowledgeandproductivity'


class QualityOfWorkModelWrapper(ProfessionalSkillsWrapper):

    model = 'bhp_personnel.qualityofwork'
