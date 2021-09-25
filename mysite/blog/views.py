from django.shortcuts import render
from django.views.generic import DetailView
from .models import Blog,Categoria
from home.views import HomeView
from django.core.paginator import Paginator
#from django.db.models import Q
# Create your views here.
class PostDetailView(HomeView):
    
    template_name="blog/post_detail.html"

    def get(self,request,str):
        
        post_of_id=Blog.objects.get(slug=str)
        self.template_name="blog/post_detail.html"
        context={}
        strval=request.GET.get('search',False)
        if strval:
            post,strval=super().search_func(request)
            self.template_name="home/home_list.html"
            paginator=Paginator(post,10)
            page_number=request.GET.get('page')
            post=paginator.get_page(page_number)

        else:
            post=Blog.objects.exclude(id=post_of_id.id).order_by('-creacion_en')[:3]

        #post=Blog.objects.filter(~Q(id=post_of_id.id)).order_by('-creacion_en')[:3]
        #https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference
        
        recent_list=Blog.objects.all().order_by('-modificado_en')[:5]
        cate=Categoria.objects.all().order_by('nombre')
        
        context={'blog_list':post,'post':post_of_id,'recent_post':recent_list,'categorias':cate,'search':strval}
        return render(request,self.template_name,context)