from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Autor,Tags,Blog
# Register your models here.
admin.site.register(Autor)
admin.site.register(Tags)
admin.site.register(Blog)