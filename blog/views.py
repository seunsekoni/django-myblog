from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

# Create your views here.
class IndexPage(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    queryset = Post.published.all()

    # def 
