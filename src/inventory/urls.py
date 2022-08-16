from django.urls import path
from .views import InventoryListView, index_page, inventory_detail

urlpatterns = [
    path('inventory', index_page, name="index"),
    path('inventory/<int:id>', inventory_detail, name='detail'),
    path('api/inventory', InventoryListView.as_view(), name="inventory-list"),
]
