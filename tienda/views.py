from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto,Cliente
from .form import PostProducto,LoginForm,CheckoutForm
from django.contrib.auth import authenticate, login

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})
def productos(request):
    Productos= Producto.objects.filter();
    return render(request, 'tienda/producto.html', {'Productos': Productos})
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

def log_in(request):
    if request.user.is_authenticated:
        return redirect('compra')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                    login(request, user)
                    return redirect('compra')
            else:
                    form.add_error(None, "Nombre de usuario o contraseña no valida")
                    return render(request, "tienda/login.html", {"form": form})

    else:
        form = LoginForm()
    return render(request, "tienda/login.html", {"form": form})


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Aquí puedes agregar la lógica para manejar la compra
            # Por ejemplo, actualizar el inventario del producto, agregar la compra al historial del usuario, etc.
            pass
    else:
        form = CheckoutForm()
    return render(request, 'tienda/checkout.html', {'form': form})




# def registro(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'tienda/registro.html', {'form': form})