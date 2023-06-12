from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    no_of_guests = models.SmallIntegerField(default=10)
    booking_date = models.DateField()

    def __str__(self):
        return self.first_name


class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    inventory = models.TextField(max_length=1000, default="")

    def __str__(self):
        return self.title