# from django.db import models
# from department.models import Department
# from django.contrib.auth.models import User
# # Create your models here.
# GENDER_CHOICES = [
#     ('Male', 'Male'),
#     ('Female', 'Female'),
#     ('Other', 'Other'),
# ]

# # EmployeePosition model 
# class EmployeePosition(models.Model):
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title

# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True) 
#     email = models.EmailField(unique=True)
#     mobile_number = models.CharField(max_length=15, blank=True, null=True)  # Mobile number 
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)  # Gender choice
#     department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True, blank=True,related_name='employees' )
#     position = models.ForeignKey('EmployeePosition', on_delete=models.SET_NULL, null=True, blank=True)
#     profile_photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)  # Profile photo
    
#     # Add permissions related to dashboard access
#     admin_access = models.BooleanField(default=False)
#     team_leader_access = models.BooleanField(default=False)
#     co_worker_access = models.BooleanField(default=False)
#     membership_access = models.BooleanField(default=False)
#     department_access = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.full_name} - {self.position.title if self.position else 'No Position'}"    
# 
from django.db import models
from department.models import Department
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class EmployeePosition(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Removed blank=True, null=True
    full_name = models.CharField(max_length=200, blank=True) 
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    position = models.ForeignKey('EmployeePosition', on_delete=models.SET_NULL, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    
    admin_access = models.BooleanField(default=False)
    team_leader_access = models.BooleanField(default=False)
    co_worker_access = models.BooleanField(default=False)
    membership_access = models.BooleanField(default=False)
    department_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.position.title if self.position else 'No Position'}"
    