from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_string_representation(self):
        item = Menu.objects.create(title="Pizza", price=10.99, inventory=100)
        self.assertEqual(str(item), "Pizza : 10.99")