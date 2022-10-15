from django.db import models


class Chef(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    receta_preferida = models.CharField(max_length=30)
    
    
    def __str__(self):
        return f"La receta preferida de {self.nombre} {self.apellido} es: {self.receta_preferida}"
    
    