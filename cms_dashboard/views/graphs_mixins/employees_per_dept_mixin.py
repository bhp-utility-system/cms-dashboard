from bhp_personnel.models import Department
from edc_base.view_mixins import EdcBaseViewMixin


class EmployeePerDeptGraphMixin(EdcBaseViewMixin):

    @property
    def dept_name_list(self):
        dept_list = []
        for dept in Department.objects.all():
            dept_list.append(dept.dept_name)
        return dept_list

    @property
    def dept_employee_count(self):
        dept_count = []
        for dept in self.dept_name_list:
            dept_count.append([dept, self.get_dept_count(dept_name=dept)])
        return dept_count

    def get_dept_count(self, dept_name):

        dept_obj = Department.objects.filter(dept_name=dept_name)
        count = dept_obj.first().employee_set.all().count()
        return count

    @property
    def dept_emp_gender_count(self):
        dept_gender_count = []
        for dept in self.dept_name_list:
            dept_gender_count.append([dept, self.get_dept_gender_count_f(dept_name=dept),
                                      self.get_dept_gender_count_m(dept_name=dept)])

        return dept_gender_count

    def get_dept_gender_count_f(self, dept_name):

        dept_gender_obj = Department.objects.filter(dept_name=dept_name)
        count = dept_gender_obj.first().employee_set.filter(gender='f').values_list(
            'identifier').distinct().count()
        return count

    def get_dept_gender_count_m(self, dept_name):

        dept_gender_obj = Department.objects.filter(dept_name=dept_name)
        count = dept_gender_obj.first().employee_set.filter(gender='m').values_list(
            'identifier').distinct().count()
        return count

    # get context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            dept_employee_data=self.dept_employee_count,
            dept_emp_gender_count=self.dept_emp_gender_count
        )
        return context
