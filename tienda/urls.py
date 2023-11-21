from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.compra, name='compra'),
    path('tienda/admin/productos', views.productos, name='productos'),
    path('tienda/admin/editar/<int:pk>', views.post_edit, name='editar'),
    path('tienda/admin/eliminar/<int:pk>', views.post_eliminar, name='eliminar'),
    path('tienda/admin/nuevo/', views.post_nuevo, name='nuevo'),
    path('tienda/mostrarBusqueda/', views.post_buscar, name='buscar'),
    path('tienda/login/', views.login, name='login'),
    path('tienda/registro/', views.registro, name="registro"),
]
