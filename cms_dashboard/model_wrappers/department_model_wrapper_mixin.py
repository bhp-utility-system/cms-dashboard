from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist


class DepartmentModelWrapperMixin:

    model = 'bhp_personnel.department'
    querystring_attrs = ['doc_identifier']
    next_url_attrs = ['doc_identifier']

    @property
    def identifier(self):
        if self.department_model_obj:
            return self.department_model_obj.identifier
        return None

    @property
    def dept_name(self):
        if self.department_model_obj:
            return self.department_model_obj.dept_name
        return None

    @property
    def department_model_obj(self):
        """Returns a department model instance or None.
        """
        try:
            return self.department_cls.objects.get(**self.department_options)
        except ObjectDoesNotExist:
            return None

    @property
    def department_cls(self):
        return django_apps.get_model('bhp_personnel.department')

    @property
    def department_options(self):
        """Returns a dictionary of options to get an existing
        department model instance.
        """
        options = dict(
            identifier=self.object.identifier)
        return options
