from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

# from .appraisal_model_wrapper import AppraisalModelWrapper


class AppraisalModelWrapperMixin:

    # appraisal_model_wrapper_cls = AppraisalModelWrapper

    @property
    def appraisal_model_cls(self):
        return django_apps.get_model('bhp_personnel.performanceassessment')

    @property
    def appraisal_model_obj(self):
        """Returns an appraisal model instance or None.
        """
        try:
            return self.appraisal_model_cls.objects.get(
                **self.appraisal_options)
        except ObjectDoesNotExist:
            return None

    # @property
    # def appraisal(self):
    #     """"Returns a wrapped saved or unsaved appraisal
    #     """
    #     model_obj = self.appraisal_model_obj or self.appraisal_model_cls(
    #         **self.create_appraisal_options)
    #     return AppraisalModelWrapper(model_obj=model_obj)

    @property
    def create_appraisal_options(self):
        """Returns a dictionary of options to create a new
        unpersisted appraisal model instance.
        """

        options = dict(
            identifier=self.identifier)
        return options

    @property
    def appraisal_options(self):
        """Returns a dictionary of options to get an existing
         appraisal model instance.
        """
        options = dict(
            identifier=self.identifier)
        return options
