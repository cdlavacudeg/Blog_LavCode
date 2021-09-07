from django.db import models
from django.db.models.fields import NullBooleanField
from ckeditor.fields import RichTextField

# Create your models here.
class Autor(models.Model):
    autor=models.CharField(max_length=250,blank=False,null=False)

    def __str__(self):
        return self.autor


class Tags(models.Model):
    tag=models.CharField(max_length=90)

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'
    def __str__(self):
        return self.tag



class Blog(models.Model):
    titulo=models.CharField(max_length=90,blank=False,null=False)
    slug=models.CharField(max_length=100,blank=False,null=False)
    descripcion=models.CharField(max_length=100,blank=False,null=False)
    imagen=models.URLField(max_length=245,blank=False,null=False)
    autor=models.ForeignKey('Autor',on_delete=models.CASCADE)
    tag=models.ForeignKey('Tags',on_delete=models.SET_NULL,null=True)
    
    #https://django-ckeditor.readthedocs.io/en/latest/#django-ckeditor
    contenido=RichTextField()

    #https://docs.djangoproject.com/en/3.2/ref/models/fields/#datefield
    creacion_en=models.DateTimeField(auto_now_add=True)
    modificado_en=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.titulo

 


