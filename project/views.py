from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import Users , Roles
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from .models import Users
from .models import Categories, Courses, CourseDetails, CourseMedia



# Create your views here.



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        # Validation for matching passwords
        if password != confirm_password:
            messages.error(request, "passwords do not match.")
            return redirect('register')

        # Check if the username or email already exists
        if Users.objects.filter(Username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if Users.objects.filter(Email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        # Create new user
        try:
            default_role = Roles.objects.get(pk=2) 
            user = Users(
                Username=username,
                Name=name,
                Email=email,
                RoleID=default_role,
                Mobile=mobile,
                RegisterDate=now().date()
            )
            # Use the set_password method to hash the password
            user.set_password(password)
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('register')

    return render(request, 'register.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, Username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')



#  logout view

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'home' with your redirect URL



#  index View

@login_required
def index(request):
    response = render(request, 'index.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    return response


#About View

def about_view(request):
    
     return render(request, 'about.html')


#courses view 

def courses_view(request):
    # Retrieve all categories, courses, course details, and course media
    categories = Categories.objects.all()
    
    # Fetch courses along with their details and media
    courses_data = []
    for category in categories:
        courses_in_category = Courses.objects.filter(CategoryID=category)
        course_details = []
        for course in courses_in_category:
            details = CourseDetails.objects.filter(CourseID=course)
            media_files = CourseMedia.objects.filter(DetailID__in=details)
            course_details.append({
                'course': course,
                'details': details,
                'media': media_files
            })
        courses_data.append({
            'category': category,
            'courses': course_details
        })

    return render(request, 'courses.html', {'courses_data': courses_data})


#Roles_View
from .services import get_all_roles

def roles_view(request):
    roles = get_all_roles()
    return render(request, 'roles.html', {'roles': roles})

