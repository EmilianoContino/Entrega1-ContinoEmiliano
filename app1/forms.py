from django import forms

class ChefFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_de_nacimiento = forms.DateField()
    receta_preferida = forms.CharField(max_length=30)
    
    