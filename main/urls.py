from django.urls import path
from main import views

urlpatterns = [
    path('home',views.index,name='home'),
    path('login/', views.login_view, name='login'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('change-password/', views.change_password, name='change_password'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/mark_read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('notifications/mark_all_read/', views.mark_all_notifications_read, name='mark_all_notifications_read'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('check-notifications/', views.check_new_notifications, name='check-notifications'),

]