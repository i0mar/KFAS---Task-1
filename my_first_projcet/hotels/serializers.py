from rest_framework import serializers
from .models import Author, Book

class AuthorsListSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Author
        fields = "__all__"

class BooksListSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = "__all__"

class AuthorDetailsSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Author
        fields = "__all__"