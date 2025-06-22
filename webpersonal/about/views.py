from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    about = About.objects.first()
    return render(request, 
                  "about/about.html",
                  {
                      "about": about,
                  }
                  )