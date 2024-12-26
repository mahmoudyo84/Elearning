from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Users

'''
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
    '''
# views.py (ملف رئيسي يشمل جميع العروض الرئيسية)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Users
from students.models import Student, Course, Enrollment
from blog.models import Course as BlogCourse

# تسجيل المستخدم
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

# تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# عرض الدورات
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# عرض تفاصيل الدورة
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    exams = course.exams.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'exams': exams})

# لوحة تحكم المستخدم
@login_required
def dashboard(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    enrollments = Enrollment.objects.select_related('student', 'course')
    return render(request, 'students/dashboard.html', {
        'students': students,
        'courses': courses,
        'enrollments': enrollments,
    })
