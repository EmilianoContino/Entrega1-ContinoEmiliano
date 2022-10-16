from django import forms

class ChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    receta_preferida = forms.CharField(max_length=30)

class BusquedaChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    