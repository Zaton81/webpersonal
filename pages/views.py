from django.shortcuts import render, get_object_or_404, redirect
from .models import Pages

# Create your views here.
def pages(request, page_id):
    page = get_object_or_404(Pages, id=page_id)
    return render(request, 'pages/pages.html', {'page': page})