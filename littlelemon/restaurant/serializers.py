from rest_framework import serializers
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
    

    def validate(self, data):
        """Ensure price > 0 and inventory >= 0"""
        if 'no_of_guests' in data and data['no_of_guests'] <= 0:
            raise serializers.ValidationError({"Number of Guests": "Numbers of Guest must be greater than 0."})
        return data


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

    
    def validate(self, data):
        """Ensure price > 0 and inventory >= 0"""
        if 'price' in data and data['price'] <= 0:
            raise serializers.ValidationError({"price": "Price must be greater than 0."})
        if 'inventory' in data and data['inventory'] < 0:
            raise serializers.ValidationError({"inventory": "Inventory cannot be negative."})
        return data