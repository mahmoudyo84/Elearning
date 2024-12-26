from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Users


# Create your views here.


# Registration View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
        return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Create your views here.
@login_required
def dashboard(request):
    # Access the related Users model instance
    custom_user = request.user.custom_user
    return render(request, 'dashboard.html', {'custom_user': custom_user})

def index(request):
    return render(request, 'index.html',)


def register(request):
    return render(request, 'register.html')


def about_view(request):
    
     return render(request, 'about.html')


def courses_view(request):
    return render(request,"courses.html")

    
def dashboard_view(request):
     return render(request, 'dashboard.html')

def dashboard_CreateEdit_Instructor_form_view(request):
    return render(request,"dashboard-CreateEdit-Instructor-form.html")

def dashboard_CreateEdit_courses_form_view(request):
    return render(request,"dashboard-CreateEdit-courses-form.html")
    
