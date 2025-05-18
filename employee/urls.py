from django.urls import path
from employee import views

urlpatterns = [
    path('add_member/', views.add_member, name='add_member'),  
    path('all_members/', views.all_members, name='all_members'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employee/update/<int:employee_id>/', views.update_employee, name='update_employee'),
]