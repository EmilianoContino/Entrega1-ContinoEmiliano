from django.db import models
from ckeditor.fields import RichTextField 

class Chef(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    receta_preferida = models.CharField(max_length=30)
    descripcion = RichTextField (blank=True, null=True)
    imagen_receta = models.ImageField(upload_to = 'fotos', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
   
    
    
    def __str__(self):
        return f"La receta preferida de {self.nombre} {self.apellido} es :  {self.receta_preferida}   "
    
    