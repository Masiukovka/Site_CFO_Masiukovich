from django.shortcuts import render
from django.http import HttpResponse

from .models import Main_paig


def index(request):
    main_page = Main_paig.objects.all()
    return render(request, 'main_page/index.html', {'main_page': main_page, 'title': "Залог финансового благополучия предприятия это:"})


    # res = "<h1>Финансы предприятия это</h1>"
    # for item in main_page:
    #     res += f'<div>\n<p>{item.title}</p></div>\n<div><p>{item.content}</p>\n</div>\n<hr>\n'
    # return HttpResponse(res)
#    return render(request, 'main_page/index.html', {'main_page': main_page})
