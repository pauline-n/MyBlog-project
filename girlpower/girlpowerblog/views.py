from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

class Home(ListView):
    # defining the model we want to use
    model = Post
    template_name = 'home.html'

class BlogDetails(DetailView):
    model = Post
    template_name = 'blog_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addblog.html'
    # fields = '__all__'
    # fields = ("title", "body")

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog.html'
    # fields = ('title', 'body')

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')