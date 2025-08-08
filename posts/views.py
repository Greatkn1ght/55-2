from django.shortcuts import render, HttpResponse
import random
from posts.models import Post

# Create your views here.

def home_page_view(request):
    return render(request, "home.html")

def html_view(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", context={"posts": posts})