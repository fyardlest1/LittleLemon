from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    no_of_guests = models.SmallIntegerField(default=10)
    booking_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} - Guests: {self.no_of_guests}'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'