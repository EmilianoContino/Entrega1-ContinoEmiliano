from django import forms
from django.

class MiFormularioDeCreacion(UserCreationForm):
    email=forms.
    password1= forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    