
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, Username, Email, Name, password=None, **extra_fields):
        if not Email:
            raise ValueError("The Email field must be set")
        if not Username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(Email)
        extra_fields.setdefault('RegisterDate', now())  # Set RegisterDate if not provided
        extra_fields.setdefault('RoleID_id', 1)
        user = self.model(Username=Username, Email=email, Name=Name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Username, Email, Name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(Username, Email, Name, password, **extra_fields)




# Roles Table
class Roles(models.Model):
    RoleID = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=255)

    def __str__(self):
        return self.RoleName


# Screens Table
class Screens(models.Model):
    ScreenID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


# Privileges Table
class Privileges(models.Model):
    RoleID = models.ForeignKey(Roles, on_delete=models.CASCADE)
    ScreenID = models.ForeignKey(Screens, on_delete=models.CASCADE)
    Action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.RoleID} - {self.ScreenID} - {self.Action}"




# Users Table
class Users(AbstractBaseUser, PermissionsMixin):
    UserID = models.AutoField(primary_key=True)
    RoleID = models.ForeignKey(Roles, on_delete=models.CASCADE)
    Username = models.CharField(max_length=255, unique=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Mobile = models.CharField(max_length=14)
    RegisterDate = models.DateField(default=now)  # Use a default value
    is_active = models.BooleanField(default=True)  # Required by Django
    is_staff = models.BooleanField(default=False)  # Required by Django
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'Username'  # Field used for authentication
    REQUIRED_FIELDS = ['Email', 'Name']  # Fields required for createsuperuser

    def __str__(self):
        return self.Username
   

# Categories Table
class Categories(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.CategoryName


# Courses Table
class Courses(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CategoryID = models.ForeignKey(Categories, on_delete=models.CASCADE)
    CourseName = models.CharField(max_length=255)

    def __str__(self):
        return self.CourseName


# CourseDetails Table
class CourseDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Duration = models.IntegerField()

    def __str__(self):
        return self.Title


# CourseMedia Table
class CourseMedia(models.Model):
    MediaID = models.AutoField(primary_key=True)
    DetailID = models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    # Path = models.CharField(max_length=255)
    MediaFile = models.FileField(upload_to='course_media/')

    def __str__(self):
        return self.MediaFile.name


# UserCourses Table
class UserCourses(models.Model):
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    RegisterDate = models.DateField()

    def __str__(self):
        return f"{self.UserID} - {self.CourseID}"


# CoursesExams Table
class CoursesExams(models.Model):
    ExamID = models.AutoField(primary_key=True)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Tile = models.CharField(max_length=255)
    Description = models.TextField()
    Degree = models.IntegerField()
    Open = models.BooleanField(default=False)
    Duration = models.IntegerField()

    def __str__(self):
        return self.Tile


# ExamsQuestions Table
class ExamsQuestions(models.Model):
    QuestionID = models.AutoField(primary_key=True)
    ExamID = models.ForeignKey(CoursesExams, on_delete=models.CASCADE)
    Question = models.TextField()
    Point = models.IntegerField()
    
    def __str__(self):
        return self.Question


# QuestionsChoices Table
class QuestionsChoices(models.Model):
    ChoiceID = models.AutoField(primary_key=True)
    ExamID = models.ForeignKey(CoursesExams, on_delete=models.CASCADE)
    QuestionID = models.ForeignKey(ExamsQuestions, on_delete=models.CASCADE)
    Choice = models.CharField(max_length=255)
    Right = models.BooleanField()

    def __str__(self):
        return self.Choice


# ExamAnswer Table
class ExamAnswer(models.Model):
    AnswerID = models.AutoField(primary_key=True)
    ExamID = models.ForeignKey(CoursesExams, on_delete=models.CASCADE)
    QuestionID = models.ForeignKey(ExamsQuestions, on_delete=models.CASCADE)
    ChoiceID = models.ForeignKey(QuestionsChoices, on_delete=models.CASCADE)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    Right = models.BooleanField()

    def __str__(self):
        return f"Answer by {self.UserID} for Question {self.QuestionID}"


# UsersExams Table
class UsersExams(models.Model):
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    ExamID = models.ForeignKey(CoursesExams, on_delete=models.CASCADE)
    Degree = models.IntegerField()

    def __str__(self):
        return f"{self.UserID} - {self.ExamID}"
        
    



