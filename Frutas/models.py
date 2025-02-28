from django.db import models
# Llamado al modelo principal de usuario
from django.contrib.auth.models import User

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Categoría: {self.nombre}'

# Create your models here.
class Fruta(models.Model):
    
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='FrutaProveedor')
    imagen = models.TextField(default='https://us.123rf.com/450wm/rashadashurov/rashadashurov2002/rashadashurov200201094/140529504-icono-de-foto-en-blanco.jpg?ver=6')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='FrutaCategoria')
    
    # Formateo para visualizar mi objeto de mejor forma
    def __str__(self):
        return f'Fruta: {self.nombre} | Precio: {self.precio}'
    
# Administrador de Django
# 1. Crear superusuario: python manage.py createsuperuser (admin, admin)