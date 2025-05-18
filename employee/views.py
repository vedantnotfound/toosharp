from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_member(request):
    departments = Department.objects.all()
    positions = EmployeePosition.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        gender = request.POST.get('gender')
        department_id = request.POST.get('department')
        position_id = request.POST.get('position')
        profile_photo = request.FILES.get('profile_photo')

        admin_access = 'admin_access' in request.POST
        team_leader_access = 'team_leader_access' in request.POST
        co_worker = 'co_worker' in request.POST
        membership_access = 'membership_access' in request.POST
        department_access = 'department_access' in request.POST
        
        if Employee.objects.filter(email=email).exists():
            # If email already exists, add an error message and redirect back
            messages.error(request, 'An employee with this email already exists.')
            return render(request, 'addmembers.html', {'departments': departments,'positions': positions})
        
        user = User.objects.create_user(username=email, email=email, password='Sharp@3232')
        user.first_name = full_name
        user.save()

        # Create an employee instance
        employee = Employee(
            user=user,
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            gender=gender,
            department_id=department_id,
            position_id=position_id,
            profile_photo=profile_photo,
            admin_access=admin_access,
            team_leader_access=team_leader_access,
            co_worker_access=co_worker,
            membership_access=membership_access,
            department_access=department_access
        )
        employee.save() 
        
        login_url ='https://task.sharpmultimedia.in/'  # Adjust the URL for your login page
        subject = "Welcome to Sharp Multimedia Task Management System"
        message = f"""
        Hello {full_name},

        You have been successfully added to the Sharp Multimedia Task Management System.

        Your login credentials are:
        Username: {email}
        Password: Sharp@3232

        Please click the link below to login and get started:
        {login_url}

        Best Regards,
        Sharp Multimedia Admin
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # Make sure to configure DEFAULT_FROM_EMAIL in settings.py
            [email],
            fail_silently=False,
        )
        
        # Redirect to another page after saving, e.g., employee list page
        return redirect('all_members')  
    return render(request, 'addmembers.html', {'departments': departments,'positions': positions})


@login_required
def all_members(request):
    employees = Employee.objects.all().order_by('-id')

    # Set the number of employees to display per page
    paginator = Paginator(employees, 5)  # 5 employees per page

    # Get the current page number from the request (default to page 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the paginated list to the template
    return render(request, 'members.html', {'page_obj': page_obj})    

@login_required
def employee_detail(request, employee_id):
    departments = Department.objects.all()
    positions = EmployeePosition.objects.all()
    # Get the employee using the ID passed in the URL
    employee = get_object_or_404(Employee, id=employee_id)

    context = {
        'employee': employee,
        'positions':positions,
        'departments':departments
    }
    return render(request, 'membersinfo.html', context)    

@login_required
def update_employee(request, employee_id):
    # Get the employee object
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        # Update the employee details from POST data
        employee.full_name = request.POST.get('full_name', employee.full_name)
        employee.mobile_number = request.POST.get('mobile_number', employee.mobile_number)
        employee.gender = request.POST.get('gender', employee.gender)
        
        # If a new profile photo is uploaded
        if 'profile_photo' in request.FILES:
            employee.profile_photo = request.FILES['profile_photo']
        
        # Handle department and position updates
        department_id = request.POST.get('department')
        if department_id != "None":
            employee.department = Department.objects.get(id=department_id)
        
        position_id = request.POST.get('position')
        if position_id != "None":
            employee.position = EmployeePosition.objects.get(id=position_id)
        
        # Handle the permissions checkboxes
        employee.admin_access = 'admin_access' in request.POST
        employee.team_leader_access = 'team_leader_access' in request.POST
        employee.co_worker = 'co_worker' in request.POST
        employee.membership_access = 'membership_access' in request.POST
        employee.department_access = 'department_access' in request.POST
        
        # Save the employee instance
        employee.save()
        
        # Redirect to the employee details page (or wherever you want after the update)
        return redirect('employee_detail', employee_id=employee.id)

    else:
        # If it's a GET request, just display the current employee data
        departments = Department.objects.all()
        positions = Position.objects.all()

        # Render the update profile form template
        return render(request, 'employee/update_employee.html', {
            'employee': employee,
            'departments': departments,
            'positions': positions,
        })
