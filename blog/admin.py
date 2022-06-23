from django.contrib import admin

from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'photo', 'content', 'created_at', 'updated_at', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'created_at', 'is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
