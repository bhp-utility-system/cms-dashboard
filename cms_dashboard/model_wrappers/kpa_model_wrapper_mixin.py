from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from .kpa_model_wrapper import KpaModelWrapper


class KpaModelWrapperMixin:

    kpa_model_wrapper_cls = KpaModelWrapper

    @property
    def kpa_model_obj(self):
        """Returns a kpa model instance or None.
        """
        try:
            return self.kpa_cls.objects.get(
                **self.kpa_options)
        except ObjectDoesNotExist:
            return None

    @property
    def kpa(self):
        """"Returns a wrapped saved or unsaved kpa
        """
        model_obj = self.kpa_model_obj or self.kpa_cls(
            **self.create_kpa_options)
        return self.kpa_model_wrapper_cls(model_obj=model_obj)

    @property
    def kpa_cls(self):
        return django_apps.get_model('bhp_personnel.keyperformancearea')

    @property
    def create_kpa_options(self):
        """Returns a dictionary of options to create a new
        unpersisted kpa model instance.
        """
        options = dict(
            emp_identifier=self.object.emp_identifier,
            contract=self.object.contract,
            assessment_period_type=self.object.assessment_period_type)
        return options

    @property
    def kpa_options(self):
        """Returns a dictionary of options to get an existing
        kpa model instance.
        """
        options = dict(
            emp_identifier=self.object.emp_identifier,
            contract=self.object.contract,
            assessment_period_type=self.object.assessment_period_type)
        return options
