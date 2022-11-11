from django.shortcuts import render

from app1.forms import BusquedaChefFormulario
from app1.models import Chef

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin # limita al usuario para no ingresar a una vista.
from django.contrib.auth.decorators import login_required # limita al usuario para no ingresar a una vista.


def index(request):
    return render(request, 'app1/index.html')

def ver_chefs(request):
    
    nombre = request.GET.get('chefs', None)
    apellido = request.GET.get('chefs', None)
    
    if nombre:
        chefs = Chef.objects.filter(nombre__icontains=nombre)        
                
    else:
        chefs = Chef.objects.all()
    
    formulario = BusquedaChefFormulario()
          
    return render(request, 'app1/ver_chefs.html', {'chefs': chefs, 'formulario': formulario})

class ListaChef(ListView):
    model = Chef
    template_name = 'app1/ver_chefs.html'
    
    # def get_queryset(self):
    #     nombre = self.request.GET.get('nombre', '')
    #     if nombre:
    #         chefs = self.model.objects.filter(nombre__icontains=nombre)
    #     else:
    #         chefs = self.model.objects.all()
    #     return chefs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["formulario"] = BusquedaChefFormulario()
    #     return context
    
    
    
    
class CrearChef(LoginRequiredMixin, CreateView):
    model = Chef
    success_url = '/app1/chefs/'
    template_name = 'app1/crear_chef.html'
    fields = ['nombre', 'apellido', 'edad', 'receta_preferida', 'descripcion', 'imagen_receta']
    
    
class EditarChef(LoginRequiredMixin, UpdateView):
    model = Chef
    success_url = '/app1/chefs/'
    template_name = 'app1/editar_chef.html'
    fields = ['nombre', 'apellido', 'edad', 'receta_preferida', 'descripcion','imagen_receta']
    
    
class EliminarChef(LoginRequiredMixin, DeleteView):
    model = Chef
    success_url = '/app1/chefs/'
    template_name = 'app1/eliminar_chef.html'
    
    

class VerChef(DetailView):
    model = Chef
    template_name = 'app1/ver_chef.html'

def about(request):

    return render(request, "app1/about.html", {})


