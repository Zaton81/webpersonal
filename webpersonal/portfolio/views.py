from django.views.generic.list import ListView
from .models import Project  # type: ignore[attr-defined]

class PortfolioView(ListView):
    """Vista de lista para mostrar los proyectos del portafolio."""
    model = Project
    template_name = "portfolio/portfolio.html"
    context_object_name = "projects"
