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
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import CoursesExams, ExamsQuestions, QuestionsChoices, ExamAnswer, UsersExams
from django.http import HttpResponseNotFound




# Create your views here.



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

# def quiz_view(request):
#     return render(request,"quiz.html")


#Roles_View
from .services import get_all_roles

def roles_view(request):
    roles = get_all_roles()
    return render(request, 'roles.html', {'roles': roles})



@login_required
def quiz_view(request, exam_id, question_index):
    # Fetch the exam details
    exam = get_object_or_404(CoursesExams, pk=exam_id)

    # Check the exam.id to make sure it's being fetched correctly
    print("Exam ID:", exam.ExamID)

    # Fetch all questions for the exam
    questions = ExamsQuestions.objects.filter(ExamID=exam)

    # Calculate total question count
    question_count = questions.count()

    # Get the specific question based on the question index
    if 0 <= question_index < question_count:
        question = questions[question_index]
    else:
        # Handle invalid question index
        return HttpResponseNotFound("Invalid question index.")

    context = {
        "exam": exam,
        "question": question,
        "question_index": question_index,
        "question_count": question_count,
    }

    return render(request, "quiz.html", context)

def submit_quiz(request):
    if request.method == "POST":
        user = request.user
        exam_id = request.POST.get("exam_id")
        answers = request.POST.getlist("answers")  # List of selected choice IDs

        exam = get_object_or_404(CoursesExams, pk=exam_id)
        score = 0
        total_points = 0

        for choice_id in answers:
            choice = get_object_or_404(QuestionsChoices, pk=choice_id)
            question = choice.QuestionID

            # Record the answer
            ExamAnswer.objects.create(
                ExamID=exam,
                QuestionID=question,
                ChoiceID=choice,
                UserID=user,
                Right=choice.Right,
            )

            # Calculate score
            if choice.Right:
                score += question.Point

            total_points += question.Point

        # Save the user's total score
        UsersExams.objects.update_or_create(
            UserID=user, ExamID=exam, defaults={"Degree": score}
        )

        return JsonResponse({"score": score, "total_points": total_points})

    return JsonResponse({"error": "Invalid request method"}, status=400)


def quiz_redirect_view(request):
    # Redirect to a default exam or handle gracefully
    return redirect('quiz', exam_id=1)

def review_quiz(request, exam_id):
    # Get the exam details
    if exam_id is None:
        exam_id = 1 
    exam = get_object_or_404(CoursesExams, pk=exam_id)
    
    # Fetch all questions for the exam
    questions = ExamsQuestions.objects.filter(ExamID=exam).select_related('ExamID')

    question_data = []
    for question in questions:
        # Fetch the choices for each question
        choices = QuestionsChoices.objects.filter(QuestionID=question)
        
        # Get user's answer (Assuming you have a model UserAnswers to store them)
        user_answer = ExamAnswer.objects.filter(QuestionID=question, UserID=request.user).first()
        
        # Prepare the question and answer data
        question_data.append({
            "id": question.QuestionID,
            "question": question.Question,
            "choices": [{"id": choice.ChoiceID, "text": choice.Choice} for choice in choices],
            "user_answer": user_answer.ChoiceID if user_answer else None
        })

    context = {
        "exam": exam,
        "questions": question_data,
        "question_index": question_index,
        "question_count": question_count,
    }
    
    return render(request, "review_quiz.html", context)

# def mark_review(request, exam_id):
#     # Get the exam object
#     exam = get_object_or_404(CoursesExams, pk=exam_id)
    
#     # Fetch the question to mark for review
#     question_id = request.POST.get('question_id')
#     question = get_object_or_404(ExamsQuestions, pk=question_id, ExamID=exam)

#     # Update or create the UserAnswer with a review flag (assuming you have a 'review' field)
#     user_answer, created = ExamAnswer.objects.update_or_create(
#         user=request.user,
#         question=question,
#         exam=exam,
#         defaults={"is_reviewed": True}  # Assuming `is_reviewed` is a Boolean field in UserAnswers
#     )

#     # Optionally, you can set a flag to mark a question as reviewed.
#     if not created:
#         # If the answer already exists, toggle the "review" status
#         user_answer.is_reviewed = not user_answer.is_reviewed
#         user_answer.save()

    # Redirect to the quiz review page or next question
    return redirect('review_quiz', exam_id=exam.id)


def previous_question(request, exam_id, question_id):
    # Get the exam object
    exam = get_object_or_404(CoursesExams, pk=exam_id)
    
    # Get the current question object
    current_question = get_object_or_404(ExamsQuestions, pk=question_id)
    
    # Find the previous question in the exam
    previous_question = ExamsQuestions.objects.filter(ExamID=exam, id__lt=current_question.id).order_by('-id').first()

    # If there is no previous question, stay on the current question
    if previous_question is None:
        return redirect('quiz', exam_id=exam.id)  # Redirect to the quiz page or the first question

    # Render the quiz page with the previous question
    context = {
        'exam': exam,
        'question': previous_question,
    }
    return render(request, 'quiz.html', context)


def review_quiz(request, exam_id):
    exam = get_object_or_404(CoursesExams, pk=exam_id)
    questions = ExamsQuestions.objects.filter(ExamID=exam)
    
    # Filter the user answers and find those marked for review
    user_answers = ExamAnswer.objects.filter(exam=exam, user=request.user)
    review_questions = [answer.question for answer in user_answers if answer.is_reviewed]
    
    context = {
        'exam': exam,
        'questions': questions,
        'review_questions': review_questions,  # Pass the review questions
    }

    return render(request, "review_quiz.html", context)

