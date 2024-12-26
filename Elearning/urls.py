"""
URL configuration for Elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from project import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    # path('', views.index, name="index"),
    path('about/', views.login_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('courses/', views.login_view, name='courses'),
    
    path('register/', views.register_view, name='register'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard-CreateEdit-Instructor-form/', views.dashboard_CreateEdit_Instructor_form_view, name='dashboard-CreateEdit-Instructor-form'),
    path('dashboard-CreateEdit-courses-form/', views.dashboard_CreateEdit_courses_form_view, name='dashboard-CreateEdit-courses-form'),
]
urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
]
