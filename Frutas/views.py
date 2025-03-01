from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Fruta, Categoria

# Create your views here.
def main(request):
    
    # Método all permite obtener todo de una tabla (SELECT * FROM tabla)
    frutas = Fruta.objects.all()
    
    return render(request, 'pages/frutas.html', {
        'frutas' : frutas
    })
    
# Este es un decorador que permite acceder a esta vista únicamente si se inició sesión
@login_required
def agregar_fruta(request):
    
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        precio = request.POST.get('precio', '').strip()
        imagen = request.POST.get('imagen', '').strip()
        # Acá estamos recibiendo un ID de categoría, NO la categoría
        categoria_id = request.POST.get('categoria')
        
        # Acá vamos a consultar el objeto de la categoría:
        categoria = Categoria.objects.get(id=categoria_id)
        
        # Hacen falta campos (parte de la tarea)
        #Ya los agregué
        try:
            # request.user es el objeto de usuario que mandó la solicitud
            fruta = Fruta(nombre = nombre,
            precio = float(precio),
            imagen = imagen,
            categoria=categoria, 
            proveedor=request.user)
            fruta.save()
        
        except Exception as e:
            print('Ocurrió un error al almacenar:', e)
        
    return render(request, 'pages/agregar_fruta.html', {
        'categorias' : categorias
    })