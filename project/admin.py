'''
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
from .models import Instructor, Course, Enrollment

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Enrollment)
##################
from django.contrib import admin
from .models import Exam, Question, Answer

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)

admin.site.register(CoursesExams)
admin.site.register(ExamsQuestions)
admin.site.register(QuestionsChoices)
admin.site.register(ExamAnswer)
admin.site.register(UsersExams)
'''
from django.contrib import admin
from .models import (
    Roles, Screens, Privileges, Users, Categories,
    Courses, CourseDetails, CourseMedia, UserCourses,
    CoursesExams, ExamsQuestions, QuestionsChoices,
    ExamAnswer, UsersExams, Instructor, Enrollment,
    Exam, Question, Answer
)

# تخصيص واجهة الإدارة لموديلات مختلفة
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'courses_taught')
    search_fields = ('name',)
    list_filter = ('courses__category',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__name', 'course__title')

class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'date_created')
    search_fields = ('title', 'course__title')

# تسجيل النماذج في واجهة الإدارة
admin.site.register(Roles)
admin.site.register(Screens)
admin.site.register(Privileges)
admin.site.register(Users)
admin.site.register(Categories)

# تسجيل الدورات
admin.site.register(Courses, CourseAdmin)
admin.site.register(CourseDetails)
admin.site.register(CourseMedia)
admin.site.register(UserCourses)

# تسجيل الامتحانات والأسئلة
admin.site.register(CoursesExams)
admin.site.register(ExamsQuestions)
admin.site.register(QuestionsChoices)
admin.site.register(ExamAnswer)
admin.site.register(UsersExams)

# تسجيل المعلمين
admin.site.register(Instructor, InstructorAdmin)

# تسجيل التسجيلات في الدورات
admin.site.register(Enrollment, EnrollmentAdmin)

# تسجيل الامتحانات والأسئلة
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question)
admin.site.register(Answer)
