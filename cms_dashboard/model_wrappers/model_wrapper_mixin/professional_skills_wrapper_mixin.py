from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist


def model_obj_cls(wrapped_model_cls):
    return django_apps.get_model(wrapped_model_cls)


class ProfessionalSkillsWrapperMixin:

    def model_obj(self, wrapped_model_cls):
        """Returns a model obj instance or None.
        """
        cls = model_obj_cls(wrapped_model_cls)
        try:
            return cls.objects.get(**self.options)
        except ObjectDoesNotExist:
            return None

    def saved_or_unsaved_model(self, wrapped_model_cls, model_wrapper_cls):
        """"Returns a wrapped saved or unsaved model
        """
        cls = model_obj_cls(wrapped_model_cls)
        model_obj = self.model_obj(wrapped_model_cls) or cls(
            **self.create_options)
        return model_wrapper_cls(model_obj=model_obj)

    @property
    def create_options(self):
        """Returns a dictionary of options to create a new
        unpersisted model instance.
        """
        options = dict(
            emp_identifier=self.object.emp_identifier,
            contract=self.object.contract,
            assessment_period_type=self.object.review)
        return options

    @property
    def options(self):
        """Returns a dictionary of options to get an existing
        model instance.
        """
        options = dict(
            emp_identifier=self.object.emp_identifier,
            contract=self.object.contract,
            assessment_period_type=self.object.review)
        return options
