from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page_view(request):
    return render(request, "home.html")

@login_required(login_url="/login")
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

@login_required(login_url="/login")
def post_detail_view(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, "posts/post_detail.html", context = {"post": post})

@login_required(login_url="/login")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm
        return render(request, "posts/post_create.html", context={"form": form})
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        else:
            player = form.cleaned_data.get("player")
            definition = form.cleaned_data.get("definition")
            image = form.cleaned_data.get("image")
            Post.objects.create(title=player, content=definition, image=image)
        return redirect("/posts")


