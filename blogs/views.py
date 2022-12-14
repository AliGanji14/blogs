from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blogs/home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogs/detail.html"
    context_object_name = "post"