from django.shortcuts import render
from home.models import Book

def home(request):
    return render (request,'home.html')

def login(request):
    return render (request,'login.html')

def bookView(request):
    return render (request,'bookView.html')

def AllBooks(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'AllBooks.html', {'books': books})
    #return render (request,'AllBooks.html')
    