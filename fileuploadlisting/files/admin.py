from django.contrib import admin

admin.site.site_header = 'HOPE administration'
admin.site.site_title = 'HOPE administration'

# Register your models here.
from .models import File

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(File, FileAdmin)