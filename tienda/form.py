from .models import Producto,Compra
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'modelo', 'unidades', 'precio', 'vip', 'marca']

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ['unidades']
class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    next = forms.CharField(widget=forms.HiddenInput, initial="/tienda")
