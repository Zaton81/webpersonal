from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from core.models import CommonInfo
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

class Posts(CommonInfo):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now())
    categories = models.ManyToManyField(Category, verbose_name='Categoría', blank=True, related_name="get_posts")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, null=True, blank=True)
    link = models.URLField(null=True, blank=True, verbose_name = "Enlace")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created']
    def __str__(self):
        return self.title
