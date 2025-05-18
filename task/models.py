from django.db import models
from employee.models import *
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    priority_choices = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    status_choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    def __str__(self):
        return self.title