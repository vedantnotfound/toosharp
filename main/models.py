from django.db import models
from django.contrib.auth.models import User
from employee.models import *
# Create your models here.
class Notification(models.Model):
    MESSAGE_CHOICES = [
        ('TASK_ASSIGNED', 'Task Assigned'),
        ('TASK_COMPLETED', 'Task Completed'),
        ('FORWARD_TASK', 'Forward Task'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    notification_type = models.CharField(max_length=50, choices=MESSAGE_CHOICES)
    message = models.CharField(max_length=255, null=True, blank=True)
    is_read = models.BooleanField(default=False)  # If the notification is read by the user
    is_seen = models.BooleanField(default=False)
    is_beep = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when notification was created

    def __str__(self):
        return f"Notification for {self.employee}: {self.message}"