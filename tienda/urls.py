from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/productos', views.productos, name='productos'),
    path('tienda/admin/editar/<int:pk>', views.post_edit, name='editar'),
    # path('tienda/admin/eliminar/<int:pk>', views.productos, name='eliminar')
    # path('tienda/admin/nuevo/<int:pk>', views.productos, name='nuevo')
   
]
