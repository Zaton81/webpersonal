from django.urls import path
from .views import LibrosView
urlpatterns = [
    path('', LibrosView.as_view(), name='libros'),
]