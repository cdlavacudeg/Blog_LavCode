from django.db import models
from django.db.models.fields import NullBooleanField
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Autor(models.Model):
    autor=models.CharField(max_length=250,blank=False,null=False)

    def __str__(self):
        return self.autor

class Categoria(models.Model):
    nombre=models.CharField(max_length=90,blank=True,unique=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    def __str__(self):
        return self.nombre

class Blog(models.Model):
    titulo=models.CharField(max_length=90,blank=False,null=False)
    slug=models.SlugField(max_length=100,blank=False,null=False,unique=True)
    descripcion=models.CharField(max_length=100,blank=False,null=False)
    imagen=models.URLField(max_length=245,blank=False,null=False)
    autor=models.ForeignKey('Autor',on_delete=models.CASCADE)
    categoria=models.ManyToManyField('Categoria')
    
    #https://django-ckeditor.readthedocs.io/en/latest/#django-ckeditor
    contenido=RichTextField()

    #https://docs.djangoproject.com/en/3.2/ref/models/fields/#datefield
    creacion_en=models.DateTimeField(auto_now_add=True)
    modificado_en=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.titulo

    def save(self,*args,**kargs):
        self.slug=slugify(self.titulo)
        super(Blog,self).save(*args,**kargs)

 


