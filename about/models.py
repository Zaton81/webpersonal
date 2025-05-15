from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='Sobre mí')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now()) #fecha de publicació
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, null=True, blank=True,) #relación con el modelo User, si se elimina el usuario se eliminan los posts
    image = models.ImageField(upload_to='projects/', verbose_name='Imagen') #sube la imagen a la carpeta projects con la fecha de subida
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación") 
    link = models.URLField(null=True, blank=True, verbose_name = "Enlace") #fecha de modificacion

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Sobre mí'
        verbose_name_plural = 'Sobre mí'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title
