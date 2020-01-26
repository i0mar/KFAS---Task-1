from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model) :
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    imageUrl = models.CharField(max_length = 1000)

    def __str__ (self) :
        return self.first_name + " " + self.last_name

class Book(models.Model) :
    title = models.CharField(max_length = 20)
    available = models.BooleanField()
    color = models.CharField(max_length = 20, choices = [("0", ""), ("1", "Green"), ("2", "Yellow"), ("3", "Blue"), ("4", "Black"), ("5", "White")], default = "0")
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__ (self) :
        return self.title