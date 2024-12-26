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

'''

from django.contrib import admin 
from .models import (
    Roles, Screens, Privileges, Users, Categories,
    Courses, CourseDetails, CourseMedia, UserCourses,
    CoursesExams, ExamsQuestions, QuestionsChoices,
    ExamAnswer, UsersExams, Instructor, Course, Enrollment,
    Exam, Question, Answer, UserProfile
)


#  Roles (الأدوار)
admin.site.register(Roles)  

#  Screens (الشاشات)
admin.site.register(Screens)  

#  Privileges (الصلاحيات)
admin.site.register(Privileges)  

#  Users (المستخدمين)
admin.site.register(Users)  

#  Categories (الفئات)
admin.site.register(Categories)  

#  Courses (الدورات)
admin.site.register(Courses)  

#  CourseDetails (تفاصيل الدورة)
admin.site.register(CourseDetails)  

#  CourseMedia (الوسائط المرتبطة بالدورة)
admin.site.register(CourseMedia)  

#  UserCourses (الدورات التي سجل فيها المستخدم)
admin.site.register(UserCourses)  

#  CoursesExams (امتحانات الدورات)
admin.site.register(CoursesExams)  

#  ExamsQuestions (أسئلة الامتحانات)
admin.site.register(ExamsQuestions)  

#  QuestionsChoices (خيارات الإجابة على الأسئلة)
admin.site.register(QuestionsChoices)  

#  ExamAnswer (إجابات الامتحانات)
admin.site.register(ExamAnswer)  

#  UsersExams (نتائج الامتحانات الخاصة بالمستخدمين)
admin.site.register(UsersExams)  

#  Instructor (المدرب)
admin.site.register(Instructor)  

#  Course (الدورة)
admin.site.register(Course)  

#  Enrollment (التسجيلات في الدورات)
admin.site.register(Enrollment)  

#  Exam (الامتحان)
admin.site.register(Exam)  

#  Question (السؤال)
admin.site.register(Question)  

#  Answer (الإجابة)
admin.site.register(Answer)  

#  UserProfile (الملف الشخصي للمستخدم)
admin.site.register(UserProfile)  
