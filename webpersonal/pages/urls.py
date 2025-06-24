from django.urls import path
from .views import PageDetailView

urlpatterns = [
    path('<int:page_id>/', PageDetailView.as_view(), name="page"),
]