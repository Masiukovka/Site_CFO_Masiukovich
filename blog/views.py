from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog, Category

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .models import Name

def index(request):
    blog = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blog': blog,
        'title': 'Мой блог',
        'categories': categories,
    }
    return render(request, template_name='blog/index.html', context=context)

def get_category(request, category_id):
    blog = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'blog/category.html', {"blog": blog, "categories": categories, "category": category})


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Сохранение формы
            form.save()
            # Редирект на ту же страницу
            return HttpResponseRedirect(request.path_info)
    else:
    # метод GET
        form = NameForm()
        # Получение всех имен из БД.
        names = Name.objects.all()
    # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
    return render(request, 'name.html', {'form': form, 'names': names})
