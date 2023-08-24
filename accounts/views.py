from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .signals import user_registered
from django.contrib.auth.models import User

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        # send the user_registered signal
        user_registered.send(sender=user.__class__, user=user)

        return HttpResponse(f"User {user.username} registered successfully!")
    return render(request, 'registration.html')

