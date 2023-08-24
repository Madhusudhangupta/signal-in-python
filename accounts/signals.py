from django.dispatch import Signal, receiver
from django.contrib.auth.models import User
from models import Notification

# define a signal
user_registered = Signal()

# connect a signal receiver
@receiver(user_registered)
def send_welcome_notification(sender, **kwargs):
    user = kwargs['user']
    print(f"Sending welcome notification to {user.username}")

    # add notification logic here
    notification = Notification.objects.create(
        user = user,
        message = f"Welcome, {user.username}! TThank you for joining us."
    )

    print(f"Sending welcome notification to {user.username}")
    