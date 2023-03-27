from django.conf import settings
from edc_model_wrapper import ModelWrapper


class ProfessionalSkillsWrapper(ModelWrapper):

    querystring_attrs = ['contract', 'emp_identifier', 'assessment_period_type']
    next_url_attrs = ['contract']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def contract(self):
        return self.object.contract
