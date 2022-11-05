from django.db import models
from django.contrib.auth.models import User


class ExtensionUsuario(models.Model):
    avatar= models.ImageField(upload_to='avatares', null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion= models.CharField(max_length=150, null=True )
    link = models.URLField(null=True)
    
    
    
