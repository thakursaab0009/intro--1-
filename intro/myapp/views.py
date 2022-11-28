from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})

def about(request):
	return render(request, 'about.html', {})

def posts(request):
	return render(request, 'post.html', {})

def contact(request):
	return render(request, 'contact.html', {})
