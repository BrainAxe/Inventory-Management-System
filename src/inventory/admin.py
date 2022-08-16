from django.contrib import admin
from .models import Supplier, Inventory


admin.site.site_header = 'Inventory Management System'                    
admin.site.index_title = 'Features area'                
admin.site.site_title = 'Inventory Management System' 


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'stock', 'availability', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']
