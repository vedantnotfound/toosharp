
from django.urls import path
from department import views

urlpatterns = [
    path('add_department/', views.add_department, name='add_department'),  
    path('all_department/', views.all_department, name='all_department'),
]