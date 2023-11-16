from django.urls import path

from . import views


app_name = 'sqli'



urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('create/', views.CreateEmployeeView.as_view(), name='employee-create'),
    path('details/', views.EmployeeDetailsView.as_view(), name='details')
]