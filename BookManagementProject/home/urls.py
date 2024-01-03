from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('bookView',views.bookView,name='bookView'),
    path('AllBooks/',views.AllBooks,name = "AllBooks")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)