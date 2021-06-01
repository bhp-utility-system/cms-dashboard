from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from .performance_imp_model_wrapper import PerformanceImpModelWrapper


class PerformanceImpModelWrapperMixin:

    performance_imp_model_wrapper_cls = PerformanceImpModelWrapper

    @property
    def performance_imp_model_obj(self):
        """Returns a performance imp  model instance or None.
        """
        try:
            return self.performance_imp_cls.objects.get(
                **self.performance_imp_options)
        except ObjectDoesNotExist:
            return None

    @property
    def performance_imp_cls(self):
        return django_apps.get_model('bhp_personnel.performanceimpplan')

    @property
    def performance_imp(self):
        """Returns a wrapped saved or unsaved performance imp.
        """
        model_obj = self.performance_imp_cls(
            **self.performance_imp_options)
        return self.performance_imp_model_wrapper_cls(model_obj=model_obj)

    @property
    def performance_imp_options(self):
        """Returns a dictionary of options to get an existing
        performance imp model instance.
        """
        options = dict(
            performance_assessment=self.object)
        return options
