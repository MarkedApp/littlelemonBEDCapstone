from django.db import models

# Create your models here.
class Booking(models.Model):
    BookingId = models.IntegerField(null=False)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    MenuId = models.IntegerField(null=False)
    ModelId = models.IntegerField(default=1)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return "{} : {}".format(self.Title, str(self.Price))
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    