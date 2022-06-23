from django.contrib import admin

from .models import About_me


class About_meAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(About_me, About_meAdmin)