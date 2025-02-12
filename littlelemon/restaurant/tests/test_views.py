from django.test import TestCase, Client
from ..models import Menu
from ..serializers import MenuSerializers
from django.urls import reverse
import json

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.ice_cream = Menu.objects.create(title="IceCream", price=8.00, inventory=100)
        self.cake = Menu.objects.create(title="Cake", price=5.50, inventory=50)
    
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

        menu = Menu.objects.all()
        expected_data = MenuSerializers(menu, many=True).data
        self.assertEqual(json.loads(response.content), expected_data)
        
