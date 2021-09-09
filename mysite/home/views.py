from django.core import paginator
from django.shortcuts import render
from django.urls import reverse
from blog.models import Blog,Autor,Categoria
from django.views import View
from django.core.paginator import Paginator
# Create your views here.
class HomeView(View):
        
    def get(self,request):
        
        recent_list=Blog.objects.all().order_by('-modificado_en')[:5]
        cate=Categoria.objects.all().order_by('nombre')
        post=Blog.objects.all().order_by('-creacion_en')
        
        #Paginador de Django https://docs.djangoproject.com/en/3.2/ref/paginator/
        paginator=Paginator(post,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)

        ctx={'blog_list':page_obj,'recent_post':recent_list,'categorias':cate}


        return render(request,'home/home_list.html',ctx)

