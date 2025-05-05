from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    image = models.ImageField(upload_to='projects/', verbose_name='Imagen') #sube la imagen a la carpeta projects con la fecha de subida
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación") #fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name= "fecha de modificación") 
    link_compra = models.URLField(null=True, blank=True, verbose_name = "Enlace de compra") #fecha de modificacion

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title