from django.shortcuts import render, redirect
from .models import Blog,Categoria
from django.core.paginator import Paginator
from django.core import paginator
from django.views import View
from home.models import Subscribers
from django.db.models import Q

# Create your views here.

class HomeView(View):
    template_name='blog/blog_list.html'
    
    def post(self,request,*args,**kargs):
        email_sub=request.POST.get('emailSub')
        if (email_sub):
            Subscribers.objects.create(email=email_sub)      
            return redirect('home:all')


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
            #https://docs.djangoproject.com/en/3.1/topics/db/queries/#complex-lookups-with-q
            query= Q(titulo__icontains=strval)| Q(contenido__icontains=strval) |Q(descripcion__icontains=strval)
            blog_list = Blog.objects.filter(query).prefetch_related().order_by('-creacion_en')
        else :
            blog_list = Blog.objects.all().order_by('-creacion_en')

        return blog_list,strval


class PostDetailView(HomeView):
    
    template_name="blog/post_detail.html"

    def get(self,request,str):
        
        post_of_id=Blog.objects.get(slug=str)
        self.template_name="blog/post_detail.html"
        context={}

        strval=request.GET.get('search',False)
        if strval:
            post,strval=super().search_func(request)
            self.template_name="blog/blog_list.html"
            paginator=Paginator(post,10)
            page_number=request.GET.get('page')
            post=paginator.get_page(page_number)

        else:
            post=Blog.objects.exclude(id=post_of_id.id).order_by('-creacion_en')[:3]
        
        recent_list=Blog.objects.all().order_by('-modificado_en')[:5]
        cate=Categoria.objects.all().order_by('nombre')
        
        context={'blog_list':post,'post':post_of_id,'recent_post':recent_list,'categorias':cate,'search':strval}
        return render(request,self.template_name,context)