from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout
from .models import Users , Roles
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password



# Create your views here.


# Registration View
# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Account created successfully!")
#         return redirect('login')
#     else:
#         form = RegisterForm()

#     return render(request, 'register.html', {'form': form})

# Login View
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request=request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')  # Redirect to the home page after login
#         else:
#             messages.error(request, 'Invalid username or password')

#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'form': form})

def profile(request):
    return render(request,'Profile.html')

def enrolled(request):
    return render(request,'enrollment.html')

def quizes(request):
    return render(request , 'exams.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if Users.objects.filter(Username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if Users.objects.filter(Email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        # Create new user
        try:
            user = Users(
                Username=username,
                Password=make_password(password),
                Name=name,
                Email=email,
                RoleID =2,
                Mobile=mobile,
                RegisterDate=now().date()
            )
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('register')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Create session for the authenticated user
            # request.session['Username'] = user.UserID
            request.session['username'] = user.username
            return redirect('index')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Ends the user's session
    return redirect('login')  # Redirect to login page after logout

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

def quiz_view(request):
    return render(request,"quiz.html")


#Roles_View
from .services import get_all_roles

def roles_view(request):
    roles = get_all_roles()
    return render(request, 'roles.html', {'roles': roles})

