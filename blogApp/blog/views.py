from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'htmlPages/home.html'
    context_object_name = 'Posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'htmlPages/post_details.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'htmlPages/post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'htmlPages/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'htmlPages/post_delete.html'
    success_url = reverse_lazy('home')