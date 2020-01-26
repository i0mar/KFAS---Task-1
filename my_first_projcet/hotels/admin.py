from django.contrib import admin
from .models import Hotel
from .models import Booking

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Booking)