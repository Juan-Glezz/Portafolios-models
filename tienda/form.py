from .models import Producto
from django import forms

class PostProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'modelo', 'unidades', 'precio', 'vip', 'marca']