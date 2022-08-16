from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Inventory
from .serializers import InventorySerializer


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'stock', 'availability']


def index_page(request):
    return render(request, 'index.html')

def inventory_detail(request, id=None):
    instance = get_object_or_404(Inventory, id=id)
    context = {
        "instance" : instance
    }
    return render(request, 'detail.html', context)
