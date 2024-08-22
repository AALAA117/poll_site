from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    "title": "Blog Post 1"
  }
  {
    "title": "Blog Post 2"
  }
]


# Create your views here.
def home(request):
  context = {
    "posts": posts
  }
  return render(request, "blog/home.html", context)

def about(request):
  return HttpResponse("<h1>Blog About</h1>")
