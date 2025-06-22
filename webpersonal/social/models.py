from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True, verbose_name='Clave del enlace') #clave del enlace
    name = models.CharField(max_length=200, verbose_name='Nombre del enlace')
    url = models.URLField(verbose_name='URL del enlace', null=True, blank=True) #url del enlace
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación") 

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name'] # ordena por fecha de creación, de más reciente a más antiguo

    def __str__(self):
        return self.name
