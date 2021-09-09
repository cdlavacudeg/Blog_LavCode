from django.shortcuts import render
from django.views.generic import DetailView
from .models import Blog,Categoria
#from django.db.models import Q
# Create your views here.
class PostDetailView(DetailView):
    model=Blog
    template_name="blog/post_detail.html"
    def get(self,request,pk):
        post_of_id=Blog.objects.get(id=pk)
        #post=Blog.objects.filter(~Q(id=post_of_id.id)).order_by('-creacion_en')[:3]
        #https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference
        post=Blog.objects.exclude(id=post_of_id.id).order_by('-creacion_en')[:3]
        recent_list=Blog.objects.all().order_by('-modificado_en')
        cate=Categoria.objects.all().order_by('nombre')
        
        context={'blog_list':post,'post':post_of_id,'recent_post':recent_list,'categorias':cate,'id_post':post_of_id.id}
        return render(request,self.template_name,context)