from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Autor,Categoria,Blog,Comment
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BlogResource(resources.ModelResource):
    class Meta:
        model=Blog

class AutorResource(resources.ModelResource):
    class Meta:
        model=Autor

class CategoriaResource(resources.ModelResource):
    class Meta:
        model=Categoria

class CommentResource(resources.ModelResource):
    class Meta:
        model:Comment


class BlogAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['titulo','descripcion','tags']
    list_display=('titulo','descripcion',)
    exclude=('slug',)
    resource_class=BlogResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class=AutorResource
    
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class=CategoriaResource

class CommentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class=CommentResource

admin.site.register(Autor,AutorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)