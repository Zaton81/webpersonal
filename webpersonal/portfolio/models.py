from django.db import models
from core.models import CommonInfo

# Create your models here.
class Project(CommonInfo):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    git_hub = models.URLField(null=True, blank=True, verbose_name = "Repositorio de Git Hub")
    order = models.SmallIntegerField(verbose_name = "orden", default = 0)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo
    def __str__(self):
        return self.title