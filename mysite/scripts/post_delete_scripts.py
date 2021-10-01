from blog.models import Blog,Autor,Categoria
from datetime import timedelta
from django.utils import timezone
def run():
    posts=Blog.objects.filter(descripcion="Prueba insersion con Scripts")
    posts.delete()