from django.contrib import admin
from .models import tessio
# Register your models here


class tessiAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'color', 'inflamacion',)
    search_fields = ('temperature', 'color', 'inflamacion',)


admin.site.register(tessio, tessiAdmin)
