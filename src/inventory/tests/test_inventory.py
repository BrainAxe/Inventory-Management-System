from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from inventory.models import Inventory, Supplier


class InventoryApiTests(TestCase):
    """Test the inventory API """

    list_url = reverse("inventory-list")

    def setUp(self):
        self.client = APIClient()

    def test_inventory_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


  
class InventoryTests(TestCase):

    def setUp(self):
        """creating supplier and inventory"""
        suppler_payload = {
            'name': 'ABC',
        }
        res = Supplier.objects.create(**suppler_payload)

        inventory_payload = {
            'name': 'Item A',
            'description': 'Item A',
            'note': 'Item A',
            'stock': 5,
            'availability': True,
            'supplier': Supplier.objects.get(id=res.id)
        }

        Inventory.objects.create(**inventory_payload)
    
    def test_inventory_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)   

    def test_inventory_detail(self):
        response = self.client.get(reverse("detail", kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)   
