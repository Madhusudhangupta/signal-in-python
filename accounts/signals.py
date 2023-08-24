from django.dispatch import Signal, receiver
from django.contrib.auth.models import User

# define a signal
user_registered = Signal()

# connect a signal receiver
@receiver(user_registered)
def send_welcome_notification(sender, **kwargs):
    user = kwargs['user']
    print(f"Sending welcome notification to {user.username}")

    # add notification logic here

    