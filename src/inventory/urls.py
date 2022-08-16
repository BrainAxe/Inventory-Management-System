from django.urls import path
from .views import InventoryListView

urlpatterns = [
    path('api/inventory', InventoryListView.as_view(), name="inventory-list"),
]
