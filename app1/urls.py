from importlib.resources import path
from django.urls import path
from app1 import views


urlpatterns = [
    
    # path('buscador/', views.buscador, name='buscador'),
    # path('buscar/', views.buscar),
    
    path('', views.index, name='inicio'),
    path('ver-chefs/', views.ver_chefs, name='ver_chefs'),
    path('chefs/', views.ListaChef.as_view(), name='ver_chefs'),
    path('chefs/crear/', views.CrearChef.as_view(), name='crear_chef'),
    path('chefs/editar/<int:pk>', views.EditarChef.as_view(), name='editar_chef'),
    path('chefs/eliminar/<int:pk>', views.EliminarChef.as_view(), name='eliminar_chef')
    
]
