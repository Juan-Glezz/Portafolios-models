from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

#El modelo Marca tiene varios campos:

#nombre, el cual es un campo de tipo CharField con una longitud máxima de 30 caracteres. 
# Además, se establece el atributo "unique=True" para garantizar que cada nombre de marca sea único en la base de datos.

#El método __str__ define cómo se debe representar una instancia de la clase Marca como una cadena de texto. 
# En este caso, solo devuelve el valor del campo nombre.

#La clase Meta se utiliza para proporcionar metadatos adicionales sobre el modelo. En este caso, 
# se establece el atributo "verbose_name_plural" como "Marcas", lo cual se utilizará para mostrar el nombre de la tabla en plural.
class Marca(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural="Marcas"
    

# La clase representa una tabla en la base de datos y tiene varios campos:

# -marca: es una ForeignKey que se relaciona con el modelo Marca y utiliza 
# la opción on_delete=models.PROTECT que protege la integridad referencial y 
# no permite eliminar una marca mientras tenga productos asociados.

# -nombre: Es de tipo CharField y tiene una longitud máxima de 50 caracteres.

# -modelo: Es de tipo CharField y tiene una longitud máxima de 50 caracteres.

# -unidades: Es de tipo PositiveIntegerField, es decir, solo acepta valores enteros positivos.

# -precio: Es de tipo DecimalField, el parámetro max_digits indica el número 
# máximo de dígitos permitidos, incluyendo decimales, y el parámetro decimal_places 
# especifica la cantidad de decimales permitidos.

# -vip: Esta línea define un campo llamado vip que es de tipo BooleanField. El parámetro 
# default=False establece el valor predeterminado como falso.

# -return f'{self.marca}{self.modelo}': Devuelve una cadena formada por la marca y el modelo del producto.

# -class Meta:  Esta línea define una clase interna llamada Meta que contiene metadatos del modelo.

# -unique_together=['marca', 'modelo']`: Esta línea establece la restricción de unicidad, lo que 
# significa que la combinación de valores de marca y modelo debe ser única en la base de datos.

class Producto(models.Model):
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    unidades = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    vip = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.marca}{self.modelo}'
    
    class Meta:
        unique_together=['marca', 'modelo']
        verbose_name_plural="Productos"

#El modelo cliente tiene los siguientes campos:

# vip: Es un campo de tipo BooleanField que representa si el cliente es VIP o no. Por defecto, se establece como False.
# saldo: Es un campo de tipo DecimalField que almacena el saldo del cliente. Permite hasta 12 dígitos en total y 2 decimales.
# user: Es un campo de tipo OneToOneField que establece una relación uno a uno con el modelo de usuario de Django settings.AUTH_USER_MODEL
# Esto significa que cada instancia de Cliente está asociada a un único usuario.
class Cliente(models.Model):
    vip = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=12,decimal_places=2)
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
    
    class Meta:
        verbose_name_plural="Clientes"

#La clase Compra es una subclase de models.Model, lo que indica que es un modelo de base de datos. Tiene varios campos:

# producto: es una clave foránea ForeignKey que apunta al modelo Producto y establece la relación de 
# uno a muchos entre la tabla Compra y Producto. También utiliza el parámetro on_delete=models.CASCADE para indicar que 
# si se elimina un producto, todas las compras relacionadas también se eliminarán.
# user: es una clave foránea que apunta al modelo Cliente y establece la relación de uno a muchos entre 
# la tabla Compra y Cliente. Al igual que el campo anterior, utiliza el parámetro on_delete=models.CASCADE 
# para manejar la eliminación en cascada.
# fecha: es un campo de fecha y hora que almacena la fecha de la compra. Se establece con el valor 
# predeterminado timezone.now, que proporciona la fecha y hora actual.
# unidades: es un campo entero que representa la cantidad de unidades compradas.
# importe: es un campo decimal que almacena el importe total de la compra.
# iva: es un campo decimal con un valor predeterminado de 0.21, que representa el impuesto sobre el valor añadido.
class Compra(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    user=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    unidades = models.IntegerField()
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    iva = models.DecimalField(max_digits=12, decimal_places=2, default=0.21)
    
    def __str__(self):
        return f'{self.user.user.username}{self.fecha}'
    
    class Meta:
        unique_together=['fecha', 'producto', 'user']
        verbose_name_plural="Compras"

# Create your models here.
