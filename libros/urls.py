from . import views as book_views
from django.urls import path
urlpatterns = [
    path('', book_views.libros, name='libros'),
]