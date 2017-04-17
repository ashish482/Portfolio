from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    # Render the index.html template
    return render(request, "blog/index.html")


def blog(request):
	posts = models.Entry.objects.all()
	return render(request, "index2.html", {'posts': posts})

def post(request, slug):
	post = get_object_or_404(models.Entry, slug = slug)
	return render(request, "post.html", {'post': post})
