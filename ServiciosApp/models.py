from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='ServiciosApp')
    created=models.DateTimeField(auto_now_add=True) 
    update=models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.titulo

class Meta:
    verbose_name='servico'
    verbose_name_plural='servicios'


