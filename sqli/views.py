from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.db import connection

from .models import Employee, ChatRoom
from .forms import EmployeeForm, ChatRoomForm


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


class EmployeeDetailsSecuredView(TemplateView):
    template_name = 'employee-details.html'

    def get(self, request, *args: Any, **kwargs):
        self.employee_id = request.GET.get('employee_id', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        sql = 'SELECT * FROM sqli_employee WHERE id = %s LIMIT 1'
        employee = Employee.objects.raw(sql, [self.employee_id])
        self.employee = employee[0] if len(employee) > 0 else None
        return {'self': self}


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class ChatRoomView(CreateView):
    template_name = 'chat-room.html'
    form_class = ChatRoomForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        sql = "INSERT INTO sqli_chatroom (message, sender) VALUES ('%s', '%s')" % (request.POST.get('message'), request.POST.get('sender'))
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)

        connection.commit()

        return HttpResponseRedirect(reverse_lazy('sqli:chat-room'))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        self.chats = ChatRoom.objects.all()
        self.form = self.get_form()
        return {'self': self}