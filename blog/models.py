from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la categoría')
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación") 
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.name

 # ordena por fecha de creación, de más reciente a más antiguo

class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now()) #fecha de publicación
    categories = models.ManyToManyField(Category, verbose_name='Categoría', blank=True, related_name="get_posts") #relación con el modelo Category, puede ser nulo o vací
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, null=True, blank=True,) #relación con el modelo User, si se elimina el usuario se eliminan los posts
    image = models.ImageField(upload_to='projects/', verbose_name='Imagen') #sube la imagen a la carpeta projects con la fecha de subida
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación") 
    link = models.URLField(null=True, blank=True, verbose_name = "Enlace") #fecha de modificacion

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title
