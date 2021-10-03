from django.shortcuts import  render
from django.core.paginator import Paginator
from django.core import paginator
from blog.views import HomeView
from blog.models import Blog,Categoria


# Create your views here.
class Home(HomeView):
    template_name='home/home.html'

    def get(self,request):
        strval=request.GET.get('search',False)
        if strval:
            self.template_name="blog/blog_list.html"
            response=super().get(request)
            return response
     
        return render(request,self.template_name)

class Subcripcion(Home):
    template_name='home/sub_ok.html'
