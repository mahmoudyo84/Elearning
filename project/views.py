from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    # Access the related Users model instance
    custom_user = request.user.custom_user
    return render(request, 'dashboard.html', {'custom_user': custom_user})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


