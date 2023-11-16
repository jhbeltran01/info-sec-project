from typing import Any
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .models import Employee
from .forms import EmployeeForm


class EmployeeListView(TemplateView):
    template_name = 'employee-list.html'

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.employees = Employee.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return {'self': self}


class CreateEmployeeView(CreateView):
    form_class = EmployeeForm
    template_name = 'employee-create.html'
    success_url = reverse_lazy('sqli:employee-create')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        self.form = self.get_form()
        return {'self': self}
    


class EmployeeDetailsView(TemplateView):
    template_name = 'employee-details.html'

    def get(self, request, *args: Any, **kwargs):
        self.employee_id = request.GET.get('employee_id', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        sql = 'SELECT * FROM sqli_employee WHERE id = ' + self.employee_id + ' LIMIT 1'
        self.employee = Employee.objects.raw(sql)[0]
        return {'self': self}