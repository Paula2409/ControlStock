from django.shortcuts import render,redirect, get_object_or_404
from django.views import generic
from .models import Producto,Proveedor
from .forms import RegistrarProducto, RegistrarProveedor
from django.urls import reverse_lazy

""" Vista basada en clase pagina inicio """
class Inicio(generic.TemplateView):
    template_name = 'index.html'
    
    def index(request):
        return render(request,'index.html')
    
""" Vistas basadas en clases productos"""
class ListaProductos(generic.ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'
    
class NuevoProducto(generic.CreateView):
    model = Producto
    template_name = 'nuevo_producto.html'
    form_class = RegistrarProducto
    success_url = reverse_lazy('productos')
    
class ModificarProducto(generic.UpdateView):
    model = Producto
    template_name = 'modificar_producto.html'
    fields = ['nombre','precio','stock_actual','proveedor']
    success_url = reverse_lazy('productos')
    
class EliminarProducto(generic.DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('productos')

""" Vistas basadas en clases proveedores """
class ListaProveedores(generic.ListView):
    model = Proveedor
    template_name = 'lista_proveedor.html'
    context_object_name = 'proveedores'

class NuevoProveedor(generic.FormView):
    model = Proveedor
    template_name = 'nuevo_proveedor.html'
    form_class = RegistrarProveedor
    success_url = reverse_lazy('proveedores')
    
class ModificarProveedor(generic.UpdateView):
    model = Proveedor
    template_name = 'modificar_proveedor.html'
    fields = ['nombre','apellido','dni']
    success_url = reverse_lazy('proveedores')
    
class EliminarProveedor(generic.DeleteView):
    model = Proveedor
    template_name = 'eliminar_proveedor.html'
    success_url = reverse_lazy('proveedores')

""" Vistas basadas en funciones """
"""
    * Producto
    def get(self,request):
        productos = Producto.objects.all() 
        return render(request,'lista_productos.html',{'productos':productos})
        
    def post(self,request):
        if request.method == 'POST':
            form = RegistrarProducto(request.POST)
            if form.is_valid():
                form.save()
                return redirect('productos')
        else:
            form = RegistrarProducto(request.POST)
        return render(request,'nuevo_producto.html',{'form': form})
        def update(self, request, pk):
        producto = get_object_or_404(Producto, id=pk)
        data={
            'form': RegistrarProducto(producto)
        }
        if request.method == 'POST':
            form = RegistrarProducto(data=request.POST,instance=producto)
            if form.is_valid():
                form.save()
                return redirect('productos', message=f'Producto {producto.nombre} modificado')
        else:
            form = RegistrarProducto(producto)
        return render(request,'productos',data)
        
    def delete(self, request, pk):
        producto_a_eliminar = get_object_or_404(Producto, id=pk)
        nombre = producto_a_eliminar.nombre
        producto_a_eliminar.delete()
        return redirect('productos', message = f'Producto {nombre} eliminado')
"""