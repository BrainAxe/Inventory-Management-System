from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Inventory
from .serializers import InventorySerializer


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'stock', 'availability']
