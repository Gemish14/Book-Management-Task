from django.shortcuts import render
from home.models import Book
from django.db.models import Q
import logging

def home(request):
    return render (request,'home.html')

def login(request):
    return render (request,'login.html')

def bookView(request):
    return render (request,'bookView.html')

def AllBooks(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'AllBooks.html', {'books': books})

def books_by_category(request, category=None):
    books = Book.objects.filter(category=category)
    return render(request, 'AllBooks.html', {'books': books, 'category': category})
    