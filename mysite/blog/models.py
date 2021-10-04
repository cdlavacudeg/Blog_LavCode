from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager


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
    comentarios=models.ForeignKey('Comment',on_delete=models.SET_NULL,blank=True,null=True)
    tags=TaggableManager(blank=True)
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

class Comment (models.Model):
    contenido=models.TextField(validators=[MinLengthValidator(3, "Comentario debe ser mayor a 3 caracteres.")])
    blog_id=models.ForeignKey('Blog',on_delete=models.CASCADE)
    nombre=models.CharField(max_length=90,blank=True,validators=[MinLengthValidator(3, "Nombre debe ser mayor a 3 caracteres.")])

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        if len(self.contenido) < 15 : return self.contenido
        return self.contenido[:11] + ' ...'
