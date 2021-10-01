from django.shortcuts import  render
from django.core.paginator import Paginator
from django.core import paginator
from blog.views import HomeView
from blog.models import Blog,Categoria


# Create your views here.
class Home(HomeView):
    template_name='home/home.html'

    def get(self,request):
        
        ctx={}
        self.template_name="home/home.html"
        strval=request.GET.get('search',False)
        if strval:
            post,strval=super().search_func(request)
            self.template_name="blog/blog_list.html"
            paginator=Paginator(post,6)
            page_number=request.GET.get('page')
            post=paginator.get_page(page_number)
            recent_list=Blog.objects.all().order_by('-creacion_en')[:4]
            cate=Categoria.objects.all().order_by('nombre')
            ctx={'blog_list':post,'recent_post':recent_list,'categorias':cate,'search':strval}


        #post=Blog.objects.filter(~Q(id=post_of_id.id)).order_by('-creacion_en')[:3]
        #https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference

        

        return render(request,self.template_name,ctx) 