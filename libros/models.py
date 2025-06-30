from django.db import models
from core.models import CommonInfo

# Create your models here.
class Books(CommonInfo):
    title = models.CharField(max_length=200, verbose_name='Título')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    link_compra = models.URLField(null=True, blank=True, verbose_name = "Enlace de compra")

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title