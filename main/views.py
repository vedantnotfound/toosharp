# from django.shortcuts import render, redirect, get_object_or_404
# from employee.models import *
# from task.models import *
# from main.models import *
# from django.core.paginator import Paginator
# from django.utils import timezone
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages

# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .models import Notification

# # Create your views here.
# @login_required
# def index(request):
#     today = timezone.now().date()
#     tasks = Task.objects.filter(date=today, employee=request.user.employee).order_by('-id')
#     employees = Employee.objects.all() 
    
#     paginator = Paginator(tasks, 10)  # 10 tasks per page
#     # Get the current page number from the request (default to page 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     context = {
#         "employees": employees,
#         "task": page_obj  
#     }
#     return render(request, 'index.html',context)



# # def check_new_notifications(request):
# #     """Returns unread notification count and latest notification ID"""
# #     unread_notifications = Notification.objects.filter(employee__user=request.user, is_read=False)

# #     latest_notification = unread_notifications.order_by('-created_at').first()  # Get the latest notification

# #     print(f"🔍 Unread Notifications: {unread_notifications.count()}")  # Debugging in Django console
# #     if latest_notification:
# #         print(f"🆕 Latest Notification ID: {latest_notification.id}")

# #     return JsonResponse({
# #         "unread_notifications": unread_notifications.count(),
# #         "latest_notification_id": latest_notification.id if latest_notification else None
# #     })

# def check_new_notifications(request):
#     new_notifications = Notification.objects.filter(employee=request.user.employee, is_seen=False,is_read=False,is_beep=False).exists()
#     notifications=Notification.objects.filter(employee=request.user.employee, is_seen=False,is_read=False,is_beep=False)
#     notifications.update(is_beep=True)
#     return JsonResponse({'new_notification': new_notifications})

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("email")
#         password = request.POST.get("password")
#         print(username)
#         print(password)
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Optionally, check if the user is an employee
#             try:
#                 # employee = Employee.objects.get(user=user)
#                 # Redirect to dashboard or specific employee page
#                 return redirect('home')  # Adjust the redirect as needed
#             except Employee.DoesNotExist:
#                 return redirect('no_employee_associated')  # Handle if no employee exists for the user
#         else:
#             messages.error(request, "Invalid credentials. Please try again." ,extra_tags='Invalid_credentials')
#             return redirect('login')
    
#     return render(request, 'login.html')  # Your login page HTML 
   
# @login_required
# def logout_view(request):
#     print("logout")
#     logout(request)
#     return redirect('login')     

# @login_required
# # Settings Created By Vedant
# def settings(request):
#      return render(request, 'settings.html')    

# @login_required
# def notifications_view(request):
#     # Get the Employee object associated with the logged-in user
#     employee = request.user.employee  # Assuming each user has an associated employee object
    
#     # Get all notifications for the logged-in user's employee
#     notifications = Notification.objects.filter(employee=employee, is_read=False).order_by('-created_at')
#     notifications.update(is_seen=True)
#     paginator = Paginator(notifications, 10)
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)
#     # Pass notifications to the template
#     return render(request, 'notifications.html', {'page_obj': page_obj})    

# @login_required
# def mark_all_notifications_read(request):
#     # Mark all notifications as read for the current user
#     notifications = Notification.objects.filter(employee=request.user.employee)
#     notifications.update(is_read=True)
    
#     return redirect('notifications')

# @login_required
# def mark_notification_read(request, notification_id):
#     notification = get_object_or_404(Notification, id=notification_id)

#     # Mark notification as read
#     notification.is_read = True
#     notification.save()

#     # Redirect back to the notifications page
#     return redirect('notifications')


# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         old_password = request.POST.get('old_password')
#         new_password = request.POST.get('new_password')
#         confirm_password = request.POST.get('confirm_password')

#         # Check if the old password is correct
#         if not request.user.check_password(old_password):
#             messages.error(request, 'Incorrect old password!')
#         elif new_password != confirm_password:
#             messages.error(request, 'New passwords do not match!')
#         else:
#             # Set the new password
#             user = request.user
#             user.set_password(new_password)
#             user.save()

#             # Update session authentication hash
#             update_session_auth_hash(request, user)

#             messages.success(request, 'Your profile has been updated.', extra_tags='profile_update')
#             return render(request, 'settings.html')

#     return render(request, 'settings.html')


# @login_required
# def update_profile(request):
#     print("hello")
#     employee = Employee.objects.get(user=request.user)
#     if request.method == 'POST':
#         # Handle the photo upload
#         if 'profile_photo' in request.FILES:
#             employee.profile_photo = request.FILES['profile_photo']
        
#         # Handle the name update
#         if 'full_name' in request.POST:
#             employee.full_name = request.POST['full_name']
        
#         employee.save()
        
#         messages.success(request, 'Your profile has been updated.', extra_tags='profile_update')
#         return redirect('settings')  # Redirect after saving to avoid resubmission

#     return render(request, 'settings.html')    

from django.shortcuts import render, redirect, get_object_or_404
from employee.models import *
from task.models import *
from main.models import *
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification
from django.core.exceptions import ObjectDoesNotExist

@login_required
def index(request):
    today = timezone.now().date()

    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        messages.error(request, "No employee profile found. Please add your profile first.")
        return redirect('add_member')  # Change 'add_member' to your actual view name for adding an employee

    tasks = Task.objects.filter(date=today, employee=employee).order_by('-id')
    employees = Employee.objects.all()

    paginator = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "employees": employees,
        "task": page_obj
    }
    return render(request, 'index.html', context)

def check_new_notifications(request):
    new_notifications = Notification.objects.filter(employee=request.user.employee, is_seen=False, is_read=False, is_beep=False).exists()
    notifications = Notification.objects.filter(employee=request.user.employee, is_seen=False, is_read=False, is_beep=False)
    notifications.update(is_beep=True)
    return JsonResponse({'new_notification': new_notifications})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                return redirect('home')
            except Employee.DoesNotExist:
                return redirect('no_employee_associated')
        else:
            messages.error(request, "Invalid credentials. Please try again.", extra_tags='Invalid_credentials')
            return redirect('login')
    
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def notifications_view(request):
    employee = request.user.employee
    notifications = Notification.objects.filter(employee=employee, is_read=False).order_by('-created_at')
    notifications.update(is_seen=True)
    paginator = Paginator(notifications, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'notifications.html', {'page_obj': page_obj})

@login_required
def mark_all_notifications_read(request):
    notifications = Notification.objects.filter(employee=request.user.employee)
    notifications.update(is_read=True)
    return redirect('notifications')

@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('notifications')

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Incorrect old password!')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match!')
        else:
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile has been updated.', extra_tags='profile_update')
            return render(request, 'settings.html')

    return render(request, 'settings.html')

@login_required
def update_profile(request):
    employee = Employee.objects.get(user=request.user)
    if request.method == 'POST':
        if 'profile_photo' in request.FILES:
            employee.profile_photo = request.FILES['profile_photo']
        if 'full_name' in request.POST:
            employee.full_name = request.POST['full_name']
        employee.save()
        messages.success(request, 'Your profile has been updated.', extra_tags='profile_update')
        return redirect('settings')

    return render(request, 'settings.html')
