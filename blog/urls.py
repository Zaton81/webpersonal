from django.urls import path
from .views import BlogListView, CategoryListView, PostDetailView 

urlpatterns = [
    path('', BlogListView.as_view(), name="blog"),
    path('category/<int:category_id>/', CategoryListView.as_view(), name="category"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post"),
]