from django.contrib import admin

from .models import Main_paig


class Main_paigAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Main_paig, Main_paigAdmin)