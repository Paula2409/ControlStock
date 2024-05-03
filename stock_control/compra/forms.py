from django import forms
from .models import Producto,Proveedor

class RegistrarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'precio',
            'stock_actual',
            'proveedor'
            ]
        # nombre = forms.CharField(label='Nombre ',max_length=100)
        # precio = forms.FloatField(label='Precio ')
        # stock_actual = forms.IntegerField(label='Stock_actual ')
        # proveedor = forms.CharField(label='Proveedor ')
    
    
class RegistrarProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'apellido',
            'dni'
            ]
    # nombre = forms.CharField(label='Nombre ',max_length=100)
    # apellido = forms.CharField(label='Apellido ', max_length=100)
    # dni = forms.IntegerField(label='Dni ')
    