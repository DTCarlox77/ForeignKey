from django.shortcuts import render
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
        nombre = ''
        precio = ''
        imagen = ''
        # Acá estamos recibiendo un ID de categoría, NO la categoría
        categoria_id = request.POST.get('categoria')
        
        # Acá vamos a consultar el objeto de la categoría:
        categoria = Categoria.objects.get(id=categoria_id)
        
        # Hacen falta campos (parte de la tarea)
        try:
            # request.user es el objeto de usuario que mandó la solicitud
            fruta = Fruta(categoria=categoria, proveedor=request.user)
            fruta.save()
        
        except Exception as e:
            print('Ocurrió un error al almacenar:', e)
        
    return render(request, 'pages/agregar_fruta.html', {
        'categorias' : categorias
    })