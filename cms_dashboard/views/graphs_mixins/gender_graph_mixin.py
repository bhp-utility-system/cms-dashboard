from bhp_personnel.models import Employee
from edc_base.view_mixins import EdcBaseViewMixin


class GenderGraphMixin(EdcBaseViewMixin):

    # gender count
    def get_gender_count(self):
        female_ids = Employee.objects.filter(gender='f').values_list(
            'identifier').distinct().count()
        male_ids = Employee.objects.filter(gender='m').values_list(
            'identifier').distinct().count()

        gender_statistics = [female_ids, male_ids]

        return gender_statistics

    gender_labels = ['Females', 'Males']

    # get context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(

            gender_labels=self.gender_labels,
            gender_stats=self.get_gender_count(),

        )
        return context
