from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Старт Блога в Django")

def about_me(request):
    return HttpResponse("Страница обо мне")