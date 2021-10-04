from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy,reverse
from .models import Blog,Categoria,Comment
from django.core.paginator import Paginator
from django.core import paginator
from django.views import View
from home.models import Subscribers
from django.db.models import Q
from django.core.mail import send_mail
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

class HomeView(View):
    template_name='blog/blog_list.html'
    
    def post(self,request,*args,**kargs):
        email_sub=request.POST.get('emailSub')
        if (email_sub):
            Subscribers.objects.create(email=email_sub)
            subject="Bienvenido a LavCode"
            message="Bienvenido a mi Blog espero que disfrutes del contenido."
            html=None
            recipient_list=[email_sub]
            send_mail(subject,message,None,recipient_list,html_message=html)
            return redirect('home:sub_ok')


    def get(self,request):
        
        recent_list=Blog.objects.all().order_by('-creacion_en')[:4]
        cate=Categoria.objects.all().order_by('nombre')
        post,search_val=self.search_func(request)
        #Paginador de Django https://docs.djangoproject.com/en/3.2/ref/paginator/
        paginator=Paginator(post,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)

        ctx={'blog_list':page_obj,'recent_post':recent_list,'categorias':cate,'search':search_val}

        return render(request,self.template_name,ctx)
    


    def search_func(self,request):

        strval=request.GET.get('search',False)
        if strval :
            #https://docs.djangoproject.com/en/3.1/topics/db/queries/#complex-lookups-with-q
            query= Q(titulo__icontains=strval)| Q(contenido__icontains=strval) |Q(descripcion__icontains=strval)|Q(tags__name__in=[strval])
            blog_list = Blog.objects.filter(query).prefetch_related().order_by('-creacion_en')
        else :
            blog_list = Blog.objects.all().order_by('-creacion_en')

        return blog_list,strval


class PostDetailView(HomeView):
    
    template_name="blog/post_detail.html"

    def post(self,request,str):
        response=super().post(request,str)

        if request.POST.get('comentario_text'):
            a = get_object_or_404(Blog, slug=str)
            logger.warning('Se crea un nuevo comentario en Post '+a.titulo)
            logger.warning('contenido del comentario: '+request.POST.get('comentario_text')+"\n")
            comment = Comment(contenido=request.POST.get('comentario_text'), blog_id=a,nombre=request.POST.get('autor_comentario'))
            comment.save()
            response=redirect(reverse('blog:post_detail', args=[str]))
        
        return response

    def get(self,request,str):
        
        post_of_id=Blog.objects.get(slug=str)
        comentarios_post=Comment.objects.filter(blog_id=post_of_id).order_by('fecha_creacion')
        self.template_name="blog/post_detail.html"
        strval=request.GET.get('search',False)
        if strval:
            self.template_name="blog/blog_list.html"
            response=super().get(request)
            return response

        post=Blog.objects.exclude(id=post_of_id.id).order_by('-creacion_en')[:3]
        recent_list=Blog.objects.all().order_by('-creacion_en')[:4]
        cate=Categoria.objects.all().order_by('nombre')
        
        context={'blog_list':post,'post':post_of_id,'recent_post':recent_list,'categorias':cate,'search':strval,'comentarios_post':comentarios_post}
        return render(request,self.template_name,context)