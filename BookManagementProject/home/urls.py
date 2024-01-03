from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('AllBooks/', views.AllBooks, name='AllBooks'),
    path('AllBooks/<str:category>/', views.books_by_category, name='books_by_category'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)