from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    dni = models.IntegerField(verbose_name='DNI')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    precio = models.FloatField(verbose_name='Precio')
    stock_actual = models.IntegerField(default=0, verbose_name='Stock actual')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, verbose_name='Proveedor')
    
    def __str__(self):
        return self.nombre
    
