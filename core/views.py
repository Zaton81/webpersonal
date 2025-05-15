from django.shortcuts import render, HttpResponse
from .links import *

# Create your views here.
def home(request):
    return render(request, "core/home.html")


                                                   
