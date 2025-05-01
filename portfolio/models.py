from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects/', verbose_name='Imagen') #sube la imagen a la carpeta projects con la fecha de subida
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación") 
    git_hub = models.URLField(null=True, blank=True, verbose_name = "Repositorio de Git Hub") #fecha de modificacion

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title