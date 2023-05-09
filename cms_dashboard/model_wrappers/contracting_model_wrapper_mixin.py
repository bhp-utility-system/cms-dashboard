from django.apps import apps as django_apps

from .contracting_model_wrapper import ContractingModelWrapper


class ContractingModelWrapperMixin:

    contracting_model_wrapper_cls = ContractingModelWrapper

    @property
    def contracting_model_obj(self):
        """Returns a contracting model instance or None.
        """
        try:
            return self.contracting_cls.objects.get(
                **self.contracting_options)
        except self.contracting_cls.DoesNotExist:
            return None

    @property
    def contracting(self):
        """"Returns a wrapped saved or unsaved contracting
        """
        model_obj = self.contracting_model_obj or self.contracting_cls(
            **self.create_contracting_options)
        return self.contracting_model_wrapper_cls(model_obj=model_obj)

    @property
    def contracting_cls(self):
        return django_apps.get_model('bhp_personnel.contracting')

    @property
    def create_contracting_options(self):
        """Returns a dictionary of options to create a new
        unpersisted contracting model instance.
        """
        options = dict(
            identifier=self.object.identifier,
            contract=self.contract
        )
        return options

    @property
    def contracting_options(self):
        """Returns a dictionary of options to get an existing
        contracting model instance.
        """
        options = dict(
            contract=self.contract,
            identifier=self.object.identifier)
        return options
