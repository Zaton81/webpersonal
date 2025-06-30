from django.views.generic.detail import DetailView
from .models import Pages  # type: ignore[attr-defined]

class PageDetailView(DetailView):
    """Vista de detalle para mostrar una página informativa gestionada desde el admin."""
    model = Pages
    template_name = 'pages/pages.html'
    context_object_name = 'page'
    pk_url_kwarg = 'page_id'