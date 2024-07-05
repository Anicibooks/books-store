urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
