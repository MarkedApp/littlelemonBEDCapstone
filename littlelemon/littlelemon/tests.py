from django.test import TestCase
from restaurant.models import Menu, MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")

class MenuViewTest(TestCase):
    def test_getall(self):
        items = Menu.objects.all()