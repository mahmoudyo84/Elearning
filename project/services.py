# services.py
from .models import Roles
from .models import Screens
from .models import Privileges
from .models import Users
from .models import Categories
from .models import Courses
from .models import CourseDetails




#Roles
def get_all_roles():
    return Roles.objects.all()

def create_role(role_name):
    role = Roles.objects.create(RoleName=role_name)
    return role

#create_screen
def get_all_screens():
    return Screens.objects.all()

def create_screen(name):
    screen = Screens.objects.create(Name=name)
    return screen

#Privileges
def get_privileges_by_role(role_id):
    return Privileges.objects.filter(RoleID=role_id)

def assign_privilege(role_id, screen_id, action):
    privilege = Privileges.objects.create(RoleID_id=role_id, ScreenID_id=screen_id, Action=action)
    return privilege

#Users
def create_user(role_id, username, password, name, email, register_date):
    user = Users.objects.create(
        RoleID_id=role_id,
        Username=username,
        Password=password,
        Name=name,
        Email=email,
        RegisterDate=register_date
    )
    return user

def get_users():
    return Users.objects.all()

#Categories
def create_category(category_name):
    category = Categories.objects.create(CategoryName=category_name)
    return category

def get_all_categories():
    return Categories.objects.all()


#Courses
def create_course(category_id, course_name):
    course = Courses.objects.create(CategoryID_id=category_id, CourseName=course_name)
    return course

def get_courses_by_category(category_id):
    return Courses.objects.filter(CategoryID_id=category_id)

#CourseDetails
def create_course_detail(course_id, user_id, title, description, duration):
    detail = CourseDetails.objects.create(
        CourseID_id=course_id,
        UserID_id=user_id,
        Title=title,
        Description=description,
        Duration=duration
    )
    return detail



