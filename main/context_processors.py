from .models import Notification

def unread_notifications(request):
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(employee=request.user.employee, is_seen=False,is_read=False).count()
        return {'unread_notifications': unread_count}
    return {'unread_notifications': 0}