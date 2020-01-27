from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Author, Book
from .serializers import AuthorsListSerializer, BooksListSerializer, AuthorDetailsSerializer, CreateAuthorSerializer, CreateBookSerializer, UpdateAuthorSerializer

# Create your views here.
class AuthorsList(ListAPIView) :
    queryset = Author.objects.all()
    serializer_class = AuthorsListSerializer

class BooksList(ListAPIView) :
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer

class AuthorDetails(RetrieveAPIView) :
    queryset = Author.objects.all()
    serializer_class = AuthorDetailsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "author_id"

class CreateAuthor(CreateAPIView) :
    serializer_class = CreateAuthorSerializer

class CreateBook(CreateAPIView) :
    serializer_class = CreateBookSerializer

class UpdateAuthor(RetrieveUpdateAPIView) :
    queryset = Author.objects.all()
    serializer_class = UpdateAuthorSerializer
    lookup_field = "id"
    lookup_url_kwarg = "author_id"

class DeleteBook(DestroyAPIView) :
    queryset = Book.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "book_id"