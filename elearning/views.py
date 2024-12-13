from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
     items = [
         {
         "title":"test",
         "description":"test"
     }
         ]
     print("hello")
     return render(request, 'about.html', {"items":items})

def login_view(request):
    return render(request, 'login.html')

def courses_view(request):
    return render(request,"courses.html")