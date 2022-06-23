from django.contrib import admin

from .models import Uslugi


class UslugiAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Uslugi, UslugiAdmin)