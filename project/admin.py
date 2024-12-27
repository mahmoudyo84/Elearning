
from django.contrib import admin

# Register your models here.
from .models import (
    Roles, Screens, Privileges, Users, Categories,
    Courses, CourseDetails, CourseMedia, UserCourses,
    CoursesExams, ExamsQuestions, QuestionsChoices,
    ExamAnswer, UsersExams
)

# Registering models in the Django admin site

admin.site.register(Roles)
admin.site.register(Screens)
admin.site.register(Privileges)
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(CourseDetails)
admin.site.register(CourseMedia)
admin.site.register(UserCourses)
from django.contrib import admin
from .models import Instructor, Course, Enrollm 
