from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import MiFormularioDeCreacion, EditarPerfilFormulario
from accounts.models import ExtensionUsuario


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm() 
    
    else:
       formulario = AuthenticationForm() 
    
    return render(request, 'accounts/login.html', {'formulario': formulario})






def mi_login(request):
    if request()
    ...



@login_required
def perfil(request):    
    extensionusuario, es_nuevo= ExtensionUsuario.objects.get_or_create(user=request.user)
    
    return render (request, 'accounts/perfil.html',{})

@login_required
def editar_perfil(request):
    
    user = request.user
    user.extensionusuario
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            user.first_name = data_nueva ['first_name']
            user.last_name = data_nueva ['last_name']
            user.email = data_nueva ['email']
            user.extensionsusuario.avatar = data_nueva ['avatar']
            
            user.extensionsusuario.save()            
            user.save()
            return redirect('perfil')
            
    else:
    formulario = EditarPerfilFormulario( initial = {
                                                    'first_name': user.first_name, 
                                                    'last_name': user.last_name,
                                                    'email': user.email,
                                                    'avatar': user.avatar,
                                                    }
                                        )
    return render (request, 'accounts/editar_perfil.html',{'formulario': formulario})

class CambiarContraseña(PasswordChangeView):

template_name = 'accounts/cambiar_contraseña.html'    
succes_url = 'acconts/perfil'    