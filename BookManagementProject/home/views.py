from django.shortcuts import render, get_object_or_404,redirect
from home.models import Book,Student
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login,logout  as django_logout
from django.contrib import messages
from django.core.mail import send_mail

import logging
logger = logging.getLogger(__name__)

#@login_required  # Requires the user to be logged in
def home(request):
    return render(request, 'home.html')

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
    error_message = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Fetch the student based on email
        try:
            student = Student.objects.get(email=email)
            password_correct = check_password(password, student.password)

            if password_correct:
                request.session['user_id'] = student.stud_id
                logger.debug("User authenticated")
                return redirect('home')
            else:
                logger.debug("Invalid username or password")
                error_message = 'Invalid username or password'
        except Student.DoesNotExist:
            logger.debug("Student does not exist")
            error_message = 'Invalid username or password'

    return render(request, 'login.html', {'error_message': error_message})
   
def logout(request):
    request.session.flush()
    django_logout(request)  # Log out the user
    return redirect('login')


def reserve_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # Sending email to the logged-in user
    if request.user.is_authenticated:
        student_email = request.user.email
        subject = f"Book Reserved: {book.title}"
        message = f"Dear {request.user.username},\n\nYou have successfully reserved the book '{book.title}'.\n\nEnjoy reading!\n\nRegards,\nAdmin"
        from_email = 'jejo14501@gmail.com'  # Replace with the admin's email or use a valid email in your system
        send_mail(subject, message, from_email, [student_email])
        messages.success(request, f"You've reserved '{book.title}'. Enjoy reading!")
    else:
        # User is not logged in
        messages.error(request, "Please log in to reserve a book.")

    return redirect('book_detail', book_id=book_id)
