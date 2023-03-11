from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['MenuId', 'ModelId', 'Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['BookingId', 'Name', 'No_of_guests', 'BookingDate']