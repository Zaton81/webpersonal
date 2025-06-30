from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Pages(models.Model):

    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name="Contenido") #contenido de la página
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación")
    order = models.SmallIntegerField(verbose_name = "orden", default = 0) 

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order','title'] # ordena por fecha de creación, de más reciente a más antiguo

    def __str__(self):
        return self.title
