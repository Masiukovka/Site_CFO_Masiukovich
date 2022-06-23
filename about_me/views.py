from django.shortcuts import render
from django.http import HttpResponse

from .models import About_me

def index(request):
    about_me = About_me.objects.all()
    return render(request, 'about_me/index.html', {'about_me': about_me, 'title': "Обо мне"})
