from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Author, Book
from .serializers import AuthorsListSerializer, BooksListSerializer, AuthorDetailsSerializer

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