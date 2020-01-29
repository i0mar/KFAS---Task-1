from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Author, Book, BorrowedBook
from .serializers import AuthorsListSerializer, BooksListSerializer, AuthorDetailsSerializer, CreateAuthorSerializer, \
    CreateBookSerializer, UpdateAuthorSerializer, CreateUserSerializer, BorrowBookSerializer, BorrowedBooksListSerializer

from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class AuthorsList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsListSerializer


class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer


class BorrowedBooksList(ListAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBooksListSerializer

    def get_queryset(self):
        return BorrowedBook.objects.filter(user = self.request.user)


class AuthorDetails(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "author_id"


class CreateAuthor(CreateAPIView):
    serializer_class = CreateAuthorSerializer


class CreateBook(CreateAPIView):
    serializer_class = CreateBookSerializer


class UpdateAuthor(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = UpdateAuthorSerializer
    lookup_field = "id"
    lookup_url_kwarg = "author_id"


class DeleteBook(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "book_id"


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer


class BorrowBook(CreateAPIView):
    queryset = BorrowedBook.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "book_id"
    serializer_class = BorrowBookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        book_id = self.kwargs.get(self.lookup_url_kwarg)
        user.save()
        serializer.save(user = user, book_id = book_id)


class UnBorrowBook(DestroyAPIView):
    queryset = BorrowedBook.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "book_id"