from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Pizza", price=10.99, inventory=100)
        self.item2 = Menu.objects.create(title="Burger", price=8.99, inventory=50)

    def test_getall(self):
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)