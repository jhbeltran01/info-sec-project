from django.urls import path

from . import views


app_name = 'sqli'



urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('sqli', views.EmployeeListView.as_view(), name='employee-list'),
    path('sqli/create/', views.CreateEmployeeView.as_view(), name='employee-create'),
    path('sqli/details/', views.EmployeeDetailsView.as_view(), name='details'),
    path('sqli/details/secured', views.EmployeeDetailsSecuredView.as_view(), name='details-secured'),
    path('chat-room/', views.ChatRoomView.as_view(), name='chat-room')
]