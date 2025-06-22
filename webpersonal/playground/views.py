from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.*

# Create your views here.
class HomePageView(TemplateView):
    template_name = "playground/playground.html"
    def get_context_data(self, **kwargs):
        #con esta función pasamos contextos como el title, etc
        context = super().get_context_data(**kwargs)
        context['title'] = "My Playground" 
        return context
    

class SamplePageView(TemplateView):
    template_name = "playground/sample.html"
    def get(self, request):
        #también se puede hacer con la función get
        return render(request, self.template_name, {"title": "Mi Web Playground"})




