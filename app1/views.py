from django.http import HttpResponse
from django.shortcuts import render

from app1.forms import BusquedaChefFormulario, ChefFormulario
from app1.models import Chef

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

def index(request):
    return render(request, 'app1/index.html')

def ver_chefs(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        chefs = Chef.objects.filter(nombre__icontains=nombre)
    else:
        chefs = Chef.objects.all()
    
    formulario = BusquedaChefFormulario()
          
    return render(request, 'app1/ver_chefs.html', {'chefs': chefs, 'formulario': formulario})

class ListaChef(ListView):
    model = Chef
    template_name = 'app1/ver_chefs.html'
    
    
class CrearChef(CreateView):
    model = Chef
    success_url = '/app1/chefs/'
    template_name = 'app1/crear_chef.html'
    fields = ['nombre', 'apellido', 'edad', 'receta_preferida']
    
    
class EditarChef(UpdateView):
    model = Chef
    success_url = '/app1/chefs/'
    template_name = 'app1/editar_chef.html'
    fields = ['nombre', 'apellido', 'edad', 'receta_preferida']
    
    
class EliminarChef(DeleteView):
    model = Chef
    success_url = '/app1/chefs/'
    template_name = 'app1/eliminar_chef.html'
    
# def buscador(request):
#     return render(request, "app1/buscador.html")

# def buscar(request):
#     if request.GET["nombre"]:
#         nombre= request.GET['nombre']
#         ver_chefs = Chef.objects.filter(nombre__icontains=nombre)
#         return render (request, "app1/buscador.html", {"nombre": nombre, "ver_chefs": ver_chefs})
    
#     else:   
#         respuesta= "No hay datos"  
    
#     return HttpResponse(respuesta)


