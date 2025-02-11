from rest_framework import serializers
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"