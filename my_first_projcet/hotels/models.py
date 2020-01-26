from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model) :
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    stars = models.IntegerField()

    def __str__ (self) :
        return self.name

class Booking(models.Model) :
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    number_of_nights = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    check_in = models.DateField()