from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

    def get_permissions(self):
        """Allow only GET requests for non-admins, full access for admins."""
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]  # Only admins can modify
        return [permissions.AllowAny()]  # Anyone can perform GET


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

    def get_permissions(self):
        """Allow only GET requests for non-admins, full access for admins."""
        if self.request.method == "GET":
            return [permissions.AllowAny()]  # Anyone can perform GET
        return [permissions.IsAdminUser()]  # Only admins can modify


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 