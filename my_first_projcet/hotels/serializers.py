from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User

class AuthorsListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = "__all__"

class BooksListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Book
        fields = "__all__"

class AuthorDetailsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = "__all__"

class CreateAuthorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = "__all__"

class CreateBookSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Book
        fields = "__all__"

class UpdateAuthorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = ['first_name', 'last_name']

class CreateUserSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only = True)

    class Meta :
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data) :
        username = validated_data['username']
        password = validated_data['password']

        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        new_user = User(username = username, first_name = first_name, last_name = last_name)
        new_user.set_password(password)
        new_user.save()

        return validated_data
