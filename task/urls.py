from django.urls import path
from task import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('incomplete_task/', views.incomplete_task, name='incomplete_task'),
    path('given_task/', views.given_task, name='given_task'),
    path('history/', views.history, name='history'),
    path('task/update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('task/update/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('task/forward_task/<int:task_id>/', views.forward_task, name='forward_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]