from django.shortcuts import render
from django.urls import reverse
from blog.models import Blog,Autor,Categoria
from django.views import View

# Create your views here.
class HomeView(View):
    
    def get(self,request):
        post=Blog.objects.all().order_by('-creacion_en')[:10]
        recent_list=Blog.objects.all().order_by('-modificado_en')[:5]
        ctx={'blog_list':post,'recent_post':recent_list}
        return render(request,'home/home_list.html',ctx)

