from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):

    email=forms.EmailField()
    password1= forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields }
        
        
        
class EditarPerfilFormulario(forms.Form):
    email=forms.EmailField()
    first_name= forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    