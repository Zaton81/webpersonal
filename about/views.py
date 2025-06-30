from .models import About  # type: ignore[attr-defined]
from django.views.generic.base import TemplateView

# Create your views here.
class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()  # type: ignore[attr-defined]
        return context