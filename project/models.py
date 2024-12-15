from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your models here.
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
class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    RoleID = models.ForeignKey(Roles, on_delete=models.CASCADE)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Mobile = models.CharField(max_length=14)
    RegisterDate = models.DateField()
    def save(self, *args, **kwargs):
        # Hash password before saving
        if not self.Password.startswith('pbkdf2_'):  # Avoid rehashing an already hashed password
            self.Password = make_password(self.Password)
        super().save(*args, **kwargs)
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
    Path = models.CharField(max_length=255)

    def __str__(self):
        return self.Path


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