from django.core import paginator
from django.shortcuts import render
from django.urls import reverse
from blog.models import Blog,Autor,Categoria
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
class HomeView(View):
    template_name='home/home_list.html'
        
    def get(self,request):
        
        recent_list=Blog.objects.all().order_by('-modificado_en')[:5]
        cate=Categoria.objects.all().order_by('nombre')
        post,search_val=self.search_func(request)
        #Paginador de Django https://docs.djangoproject.com/en/3.2/ref/paginator/
        paginator=Paginator(post,10)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)

        ctx={'blog_list':page_obj,'recent_post':recent_list,'categorias':cate,'search':search_val}


        return render(request,self.template_name,ctx)

    def search_func(self,request):

        strval=request.GET.get('search',False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(titulo__icontains=strval)
            #query.add(Q(contenido__icontains=strval), Q.OR)
            blog_list = Blog.objects.filter(query).select_related().order_by('-creacion_en')
        else :
            blog_list = Blog.objects.all().order_by('-creacion_en')

        return blog_list,strval


    

