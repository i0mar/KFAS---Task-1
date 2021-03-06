"""my_first_projcet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotels.views import *
from hotels.models import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/list/', AuthorsList.as_view()),
    path('books/list/', BooksList.as_view()),
    path('authors/<int:author_id>/', AuthorDetails.as_view()),
    path('authors/', CreateAuthor.as_view()),
    path('books/', CreateBook.as_view()),
    path('authors/update/<int:author_id>/', UpdateAuthor.as_view()),
    path('books/remove/<int:book_id>/', DeleteBook.as_view()),
    path('register/', CreateUser.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('books/borrow/<int:book_id>/', BorrowBook.as_view()),
    path('books/unborrow/<int:book_id>/', UnBorrowBook.as_view()),
    path('books/borrowed/', BorrowedBooksList.as_view())
]