from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from core.models import CommonInfo
# Create your models here.

class About(CommonInfo):
    title = models.CharField(max_length=200, verbose_name='Sobre mí')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now()) #fecha de publicació
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, null=True, blank=True,) #relación con el modelo User, si se elimina el usuario se eliminan los posts
    link = models.URLField(null=True, blank=True, verbose_name = "Enlace") #fecha de modificacion

    class Meta:
        verbose_name = 'Sobre mí'
        verbose_name_plural = 'Sobre mí'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title
