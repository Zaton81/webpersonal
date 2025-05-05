from django.shortcuts import render, get_object_or_404
from .models import Posts, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog(request):
    posts = Posts.objects.all()
    return render(request, 
                  "blog/blog.html",
                  {
                      "posts": posts,
                  }
                  )

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # con get_object_or_404 se obtiene el objeto o se lanza un error 404 si no existe
    #posts = Posts.objects.filter(categories=category,)  # se filtran los posts por la categoria
    return render(request, 
                  "blog/category.html",
                  {
                      "category": category,
                        #"posts": posts,
                  }
                  )