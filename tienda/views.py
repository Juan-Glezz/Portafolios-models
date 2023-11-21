from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .form import PostProducto

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})
def productos(request):
    Productos= Producto.objects.filter();
    return render(request,'tienda/productos.html', {'Productos':Productos})
def compra(request):
    Productos= Producto.objects.filter();
    return render(request,'tienda/compra.html', {'Productos':Productos})

def post_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = PostProducto(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('productos')
    else:
        form = PostProducto(instance=producto)
    return render(request, 'tienda/editar.html', {'form': form, 'pk': pk})
 
def post_eliminar(request, pk):
    producto=Producto.objects.filter(pk=pk).delete() 
    return redirect('productos')


def post_nuevo(request):
    if request.method == 'POST':
        form = PostProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = PostProducto()
    
    return render(request, 'tienda/nuevo.html', {'form': form})

def post_buscar(request):
    busqueda = request.GET.get("buscar_post")
    Productos = Producto.objects.filter(nombre=busqueda)
    return render(request, 'tienda/mostrarBusqueda.html', {'Productos': Productos , "busqueda": busqueda})


