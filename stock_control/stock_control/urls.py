from django.contrib import admin
from django.urls import path, include
from compra import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.Inicio.as_view(), name='inicio'),
    path('productos/', views.ListaProductos.as_view(), name='productos'),
    path('nuevo_producto/', views.NuevoProducto.as_view(), name='nuevo_producto'),
    path('modificar_producto/<int:pk>', views.ModificarProducto.as_view(), name='modificar_producto'),
    path('eliminar_producto/<int:pk>/', views.EliminarProducto.as_view(), name='eliminar_producto'),
    path('proveedores/', views.ListaProveedores.as_view(), name='proveedores'),
    path('nuevo_proveedor/', views.NuevoProveedor.as_view(), name='nuevo_proveedor'),
    path('modificar_proveedor/<int:pk>', views.ModificarProveedor.as_view(), name='modificar_proveedor'),
    path('eliminar_proveedor/<int:pk>/', views.EliminarProveedor.as_view(), name='eliminar_proveedor'),
]
