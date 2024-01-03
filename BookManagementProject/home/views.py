from django.shortcuts import render, get_object_or_404
from home.models import Book

def home(request):
    return render (request,'home.html')

def login(request):
    return render (request,'login.html')

def AllBooks(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'AllBooks.html', {'books': books})

def books_by_category(request, category=None):
    books = Book.objects.filter(category=category)
    return render(request, 'AllBooks.html', {'books': books, 'category': category})

def book_detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id) #pk = primarykey
    return render(request,'bookView.html',{'book': book})