from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="blog"),
    path('blog/category/<int:category_id>/', get_category, name="category_id"),
    ]
