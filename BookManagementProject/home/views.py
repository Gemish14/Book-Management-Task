from django.shortcuts import render, get_object_or_404,redirect
from home.models import Book,Student
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login,logout  as django_logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


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
    
    if request.session.get('user_id'):
        user_id = request.session['user_id']
        try:
            student = Student.objects.get(pk=user_id)
            student_email = student.email
            subject = f"Book Reserved: {book.title}"
            message = f"Dear {student.name},\n\nYou have successfully reserved the book '{book.title}'.\n\nEnjoy reading!\n\nRegards,\nAdmin"
            from_email = settings.EMAIL_HOST_USER
            
            try:
                send_mail(subject, message, from_email, [student_email], fail_silently=False)
                messages.success(request, f"You've reserved '{book.title}'. Enjoy reading!")
            except Exception as e:
                # Handle email sending failure
                messages.error(request, f"Failed to reserve the book. Error: {e}")
        except Student.DoesNotExist:
            messages.error(request, "User does not exist.")
    else:
        messages.error(request, "Please log in to reserve a book.")
    return redirect('book_detail', book_id=book_id)
