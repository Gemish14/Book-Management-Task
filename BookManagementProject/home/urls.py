from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('bookView',views.bookView,name='bookView'),
    path('AllBooks/',views.AllBooks,name = "AllBooks")
]