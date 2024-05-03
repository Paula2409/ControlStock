from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Producto,Proveedor

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','stock_actual','proveedor')
    list_filter = ('proveedor',)

admin.site.register(Producto,ProductoAdmin)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni')
