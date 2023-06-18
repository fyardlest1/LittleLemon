from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Menu.objects.create(title="Patate", price=8, inventory=150)
    
    def test_getall(self):
        menu = Menu.objects.get()
        expected_object_title = f'{menu.title} : {menu.price}'
        self.assertEqual(str(menu), expected_object_title)