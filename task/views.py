from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Task, Employee
from main.models import Notification
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    return render(request, 'dashboard.html', {'notifications': notifications})

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.
# Add task view 
@login_required
def add_task(request):
    today = timezone.now().date()
    print("in add task view ")
    if request.method == "POST":
        # Collecting form data from the POST request
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        member_id = request.POST.get('member')
        date = request.POST.get('date')
        assigned_by = request.user.employee

        # Retrieve the Employee object from the member_id
        member = Employee.objects.get(id=member_id) if member_id else None
        

        task = Task(
            title=title,
            description=description,
            priority=priority,
            employee=member,
            date=date,
            assigned_by=assigned_by
        )
        task.save() 

        notification_message = f"You have been assigned a task: {task.title} by {assigned_by} "
        
        Notification.objects.create(
            employee=task.employee, 
            notification_type="TASK_ASSIGNED",
            message=notification_message
        )
        
        return redirect('add_task')
        

    task = Task.objects.filter(date=today, employee=request.user.employee).order_by('-id')
    employees = Employee.objects.all() 
    # Set up pagination: Show 10 tasks per page (you can adjust this number)
    paginator = Paginator(task, 10)  # 10 tasks per page
    # Get the current page number from the request (default to page 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "employees": employees,
        "task": page_obj  # Use the paginated page object
    }
    return render(request, 'index.html',context)

@login_required
def upcoming(request):
    today = timezone.now().date()
    task = Task.objects.filter(date__gt=today, employee=request.user.employee).order_by('-id')
    paginator = Paginator(task, 10)  # 10 tasks per page
    # Get the current page number from the request (default to page 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "task": page_obj  
    }
    return render(request, 'upcoming.html',context) 

@login_required
def incomplete_task(request):
    today = timezone.now().date()
    task = Task.objects.filter( date__lt=today, status__in=['Pending', 'In Progress', 'On Hold'], employee=request.user.employee).order_by('-id')
    paginator = Paginator(task, 10)  # 10 tasks per page
    # Get the current page number from the request (default to page 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "task": page_obj  
    }
    return render(request, 'incompleted.html',context)  

@login_required
def given_task(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(assigned_by=request.user.employee).order_by('-id')    
    employees = Employee.objects.all() 
    
    paginator = Paginator(tasks, 10)  # 10 tasks per page
    # Get the current page number from the request (default to page 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "task": page_obj,
        "employees": employees, 
    }
    return render(request, 'given_task.html',context)           

@login_required
def history(request):
    today = timezone.now().date()
    task = Task.objects.filter(status='Completed', employee=request.user.employee).order_by('-id')

    paginator = Paginator(task, 10)  # 10 tasks per page
    # Get the current page number from the request (default to page 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "task": page_obj  
    }
    return render(request, 'history.html',context)     


@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    old_status= task.status
    if request.method == 'POST':
        # Get the selected status from the form submission
        new_status = request.POST.get('status')

        # Validate and update the status
        if new_status in ['Pending', 'In Progress', 'On Hold', 'Completed']:
            task.status = new_status
            task.save()

        
        notification_message = f"The task '{task.title}' assigned to {task.employee.full_name} has been updated status from '{old_status}' to '{task.status}' by {task.employee.full_name}."        
        Notification.objects.create(
            employee=task.assigned_by,
            message=notification_message,
            notification_type="TASK_COMPLETED"
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    # If GET request (optional, in case you want to render a form with task info)
    return render(request, 'task_detail.html', {'task': task})    


# @login_required
# def update_task(request, task_id):
#     print("update")
#     task = get_object_or_404(Task, id=task_id)
#     old_task= task
#     if request.method == 'POST':
#         # Get the selected status from the form submission
#         newtitle = request.POST.get('title')
#         description = request.POST.get('description')
#         date = request.POST.get('date')
#         priority = request.POST.get('priority')
#         member = request.POST.get('member')
#         print(newtitle)
#         print(description)
#         print(date)
#         print(priority)
#         print(member)
#         # Validate and update the status
        
        
#         task.title = newtitle
#         task.save()
        
#         notification_message = f"The task '{task.title}' assigned to {task.employee.full_name} has been updated"        
#         Notification.objects.create(
#             employee=task.assigned_by,
#             message=notification_message,
#             notification_type="TASK_COMPLETED"
#         )
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
#     # If GET request (optional, in case you want to render a form with task info)
#     return render(request, 'task_detail.html', {'task': task})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    old_task= task
    if request.method == 'POST':
        # Get the selected status from the form submission
        newtitle    = request.POST.get('title')
        description = request.POST.get('description')
        date        = request.POST.get('date')
        priority    = request.POST.get('priority')
        # Validate and update the status
        task.title = newtitle
        task.description = description
        task.date = date
        task.priority = priority
        task.save()
        notification_message = f"The task '{task.title}' assigned to {task.employee.full_name} has been updated"
        Notification.objects.create(
            employee=task.assigned_by,
            message=notification_message,
            notification_type="TASK_COMPLETED"
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # If GET request (optional, in case you want to render a form with task info)
    return render(request, 'index.html', {'task': task})


@login_required
def forward_task(request, task_id):
    print("ft")
    task = get_object_or_404(Task, id=task_id)
    forward_task_from = task.employee

    if request.method == "POST":
        member_id = request.POST.get('member')
        print(member_id)
        # Check if a member is selected
        if member_id != "None":
            selected_member = Employee.objects.get(id=member_id)
            print(selected_member)
            task.employee = selected_member  # Update the task's assigned employee
            task.save()  # Save the changes
            notification = Notification.objects.create(
                employee=task.employee,
                notification_type='TASK_ASSIGNED',
                message=f"You have been forwarded the task: {task.title} by {forward_task_from}",
                is_read=False
            )
            notification.save()
            notification = Notification.objects.create(
                employee=forward_task_from,
                notification_type='FORWARD_TASK',
                message=f"Your {task.title} task have been forwarded to {task.employee}",
                is_read=False
            )
            notification.save()
            messages.success(request, "Task forwarded successfully.")
        else:
            messages.error(request, "Please select a member to forward the task.")

        # Redirect back to the task or a relevant page
        return redirect('home')  # You can redirect to the task details page or wherever you'd like

    # If the request is GET (which it shouldn't be for this view), return a 404 or redirect
    return redirect('home')  # Alternatively, redirect to another page if needed    

def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, "Task deleted successfully!")
    return redirect(request.META.get("HTTP_REFERER", "index"))  # Redirect back   