from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blogs/home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogs/post_detail.html"
    context_object_name = "post"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blogs/post_new.html"
    fields = ["title", "author", "body"]



class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blogs/post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blogs/post_delete.html"
    success_url = reverse_lazy("home")
