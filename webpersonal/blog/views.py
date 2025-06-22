from django.shortcuts import get_object_or_404
from .models import Posts, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class BlogListView(ListView):
    model = Posts

#cambiamos el modelo para trabajar con clases
'''def blog(request):
    posts = Posts.objects.all()
    return render(request, 
                  "blog/blog.html",
                  {
                      "posts": posts,
                  }
                  )'''

class CategoryListView(ListView):
    model = Posts
    template_name = "blog/category.html"
    context_object_name = "posts"

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Posts.objects.filter(categories__id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context
'''def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # con get_object_or_404 se obtiene el objeto o se lanza un error 404 si no existe
    #posts = Posts.objects.filter(categories=category,)  # se filtran los posts por la categoria
    return render(request, 
                  "blog/category.html",
                  {
                      "category": category,
                        #"posts": posts,
                  }
                  )
'''
class PostDetailView(DetailView):

    model = Posts
    template_name = "blog/post.html"
    context_object_name = "post"



'''def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, "blog/post.html", {"post": post})'''



