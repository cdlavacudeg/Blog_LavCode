from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Autor,Tags,Blog
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BlogResource(resources.ModelResource):
    class Meta:
        model=Blog


class BlogAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['titulo','descripcion','tags']
    list_display=('titulo','descripcion',)
    resource_class=BlogResource


admin.site.register(Autor)
admin.site.register(Tags)
admin.site.register(Blog,BlogAdmin)