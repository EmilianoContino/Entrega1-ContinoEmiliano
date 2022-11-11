from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

class MiFormularioDeCreacion(UserCreationForm):

    email=forms.CharField()
    password1= forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields }
        
        
        
class EditarPerfilFormulario(forms.Form):
    email=forms.CharField()
    first_name= forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    descripcion = forms.CharField(label='Contanos tu experiencia', widget=forms.Textarea, required=False)
    link = forms.URLField(label='Link de mi Pagina', required=False)
    
    
    

class MiCambioContraseña (PasswordChangeForm):
    old_password = forms.CharField(label = "Contraseña Vieja", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label = "Contraseña Nueva", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label = "Repetir Contraseña Nueva", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields }
        
        