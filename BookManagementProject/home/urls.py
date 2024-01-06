from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings
#from django.views.generic import RedirectView

urlpatterns = [
    #path('', RedirectView.as_view(url='login/')),
    path('', views.home, name='home'),
    path('AllBooks/', views.AllBooks, name='AllBooks'),
    path('AllBooks/<str:category>/', views.books_by_category, name='books_by_category'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reserve/<int:book_id>/', views.reserve_book, name='reserve_book'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)