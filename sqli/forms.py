from django import forms

from .models import Employee, ChatRoom


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'department'
        ]


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = [
            'message',
            'sender'
        ]