from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created')  # Campos visibles en la lista
    search_fields = ('title', 'content')  # Campos para la barra de búsqueda
    list_filter = ('author', 'published')  # Filtros laterales
    ordering = ('-published',)  # Orden predeterminado