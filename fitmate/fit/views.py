from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def index(request):
    return render(request, 'fit/index.html')

def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'fit/register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['passweord']
        user = authenticate(request , email = email , password = password)

        if user is not None:
            login(request , user)
            return redirect('dashboard')
        else:
            messages.error(request , 'Invalid Password or Email id')
    else:
        return render(request,'fit/login.html')
# Create your views here.
