from django import forms
from ckeditor.fields import RichTextFormField

class ChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    receta_preferida = forms.CharField(max_length=30)
    descripcion = RichTextFormField (required=False)
    imagen_receta = forms.ImageField(label = 'Imagen de tu Receta', required=False)
    # fecha_creacion = forms.DateField(required=False)

class BusquedaChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    
    
    
    
    