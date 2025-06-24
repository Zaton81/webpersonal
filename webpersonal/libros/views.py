from django.views.generic.list import ListView
from .models import Books  # type: ignore[attr-defined]

class LibrosView(ListView):
    """Vista de lista para mostrar los libros."""
    model = Books
    template_name = "libros/libros.html"
    context_object_name = "books"
