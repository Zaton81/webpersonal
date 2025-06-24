from django.shortcuts import get_object_or_404
from .models import Posts, Category  # type: ignore[attr-defined]
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class BlogListView(ListView):
    """Vista de lista para mostrar todos los posts del blog."""
    model = Posts



class CategoryListView(ListView):
    """Vista de lista para mostrar los posts filtrados por categoría."""
    model = Posts
    template_name = "blog/category.html"
    context_object_name = "posts"

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Posts.objects.filter(categories__id=category_id)  # type: ignore[attr-defined]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context

class PostDetailView(DetailView):
    """Vista de detalle para mostrar un post individual."""
    model = Posts
    template_name = "blog/post.html"
    context_object_name = "post"







