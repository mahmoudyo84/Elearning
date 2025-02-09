from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Users


# Create your views here.

def index(request):
    return render(request, 'index.html')


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