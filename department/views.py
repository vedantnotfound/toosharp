from django.shortcuts import render, redirect
from .models import Department
from employee.models import Employee
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all_department(request):
    departments = Department.objects.all().order_by('-id')
    for department in departments:
        department.employee_count = department.employees.count()
    return render(request, 'department/alldepartment.html', {'departments': departments}) 


@login_required
def add_department(request):
    if request.method == 'POST':
        # Get data from the form
        dept_name = request.POST.get('dept_name')
        team_head_id = request.POST.get('team_head')
        team_leader_id = request.POST.get('team_leader')

        # Handle department creation
        if dept_name:
            # Retrieve employees from the database for team head and leader
            team_head = Employee.objects.get(id=team_head_id) if team_head_id else None
            team_leader = Employee.objects.get(id=team_leader_id) if team_leader_id else None

            # Create a new department instance
            department = Department.objects.create(
                title=dept_name,
                team_head=team_head,
                team_leader=team_leader
            )

            # Optionally, redirect after successful creation (or stay on the same page)
            return redirect('add_department')  # Redirect to a view that displays departments, for example

    # If not a POST request, or if form data is invalid, just render the empty form
    employees = Employee.objects.all()  # Get all employees to populate the dropdown
    
    return render(request, 'department/adddepartment.html', {'employees': employees}) 
