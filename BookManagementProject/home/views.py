from django.shortcuts import render, get_object_or_404,redirect
from home.models import Book,Student
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
import logging
logger = logging.getLogger(__name__)

#@login_required  # Requires the user to be logged in
def home(request):
    # Fetch the user's name if user ID is present in the session
    user_id = request.session.get('user_id')
    user_name = None
    if user_id:
        try:
            user = Student.objects.get(stud_id=user_id)
            user_name = user.name
        except Student.DoesNotExist:
            pass
    return render(request, 'home.html', {'name': user_name})

def AllBooks(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'AllBooks.html', {'books': books})

def books_by_category(request, category=None):
    books = Book.objects.filter(category=category)
    return render(request, 'AllBooks.html', {'books': books, 'category': category})

def book_detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id) #pk = primarykey
    return render(request,'bookView.html',{'book': book})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        stud_id = request.POST.get('stud_id')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email already exists in the database
        if Student.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'User already exists'})

        # Hash the password before saving
        hashed_password = make_password(password)

        # Create a new Student instance and save it to the database
        new_student = Student(name=name, stud_id=stud_id, email=email, password=hashed_password)
        new_student.save()

        # Redirect to the login page after successful signup
        return redirect('login')

    return render(request, 'signup.html')

def login(request):   
    error_message = None  # Initialize error message

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(email=email)
            password_correct = check_password(password, student.password)

            if password_correct:
                # Authentication successful
                request.session['user_id'] = student.stud_id
                return redirect('home')
            else:
                # Incorrect password
                error_message = 'Invalid email or password'
        except Student.DoesNotExist:
            # Student with provided email does not exist
            error_message = 'Invalid email or password'

    # Return the login form with the error message if applicable
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')
   