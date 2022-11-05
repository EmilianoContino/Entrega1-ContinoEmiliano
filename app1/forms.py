from django import forms
from ckeditor.fields import RichTextFormField

class ChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    receta_preferida = forms.CharField(max_length=30)
    descripcion = RichTextFormField (required=False)
    # avatar = forms.ImageField(required=False)

class BusquedaChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    # apellido = forms.CharField(max_length=30, required=False)
    
    
    
    