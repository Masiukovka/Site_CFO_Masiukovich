from django.shortcuts import render
from django.http import HttpResponse

from .models import Uslugi


def index(request):
    uslugi = Uslugi.objects.all()
    return render(request, 'uslugi/index.html', {'uslugi': uslugi, 'title': "Для финансового благополучия Вашего бизнеса"})
