from django.db import models
# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=255)
    
    # Use a string-based reference to the 'Employee' model in the 'employee' app
    team_leader = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_leader')
    team_head = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_head')

    def __str__(self):
        return self.title