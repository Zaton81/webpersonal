from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    image = models.ImageField(upload_to='projects/', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificación")

    class Meta:
        abstract = True
