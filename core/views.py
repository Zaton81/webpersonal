from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    """Vista para mostrar la página de inicio."""
    template_name = "core/home.html"


                                                   
