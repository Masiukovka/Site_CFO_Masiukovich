from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog


def index(request):
    blog = Blog.objects.all()
    return render(request, 'blog/index.html', {'blog': blog, 'title': "Мой блог"})
