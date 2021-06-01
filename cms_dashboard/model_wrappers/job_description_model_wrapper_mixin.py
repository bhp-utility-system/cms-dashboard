from django.apps import apps as django_apps

from .job_description_model_wrapper import JobDescriptionModelWrapper


class JobDescriptionModelWrapperMixin:

    job_description_model_wrapper_cls = JobDescriptionModelWrapper

    @property
    def job_description_model_obj(self):
        """Returns a job description model instance or None.
        """
        try:
            return self.job_description_cls.objects.get(
                **self.job_description_options)
        except self.job_description_cls.DoesNotExist:
            return None

    @property
    def job_description(self):
        """"Returns a wrapped saved or unsaved job description
        """
        model_obj = self.job_description_model_obj or self.job_description_cls(
            **self.create_job_description_options)
        return self.job_description_model_wrapper_cls(model_obj=model_obj)

    @property
    def job_description_cls(self):
        return django_apps.get_model('bhp_personnel.jobdescription')

    @property
    def create_job_description_options(self):
        """Returns a dictionary of options to create a new
        unpersisted job description model instance.
        """
        options = dict(
            identifier=self.contract.identifier,
            contract=self.contract)
        if hasattr(self, 'employee_model_obj'):
            options.update(
                job_title=self.employee_model_obj.job_title,
                supervisor=self.employee_model_obj.supervisor,
                department=self.employee_model_obj.department)
        return options

    @property
    def job_description_options(self):
        """Returns a dictionary of options to get an existing
        job description model instance.
        """
        options = dict(
            contract=self.contract)
        return options
