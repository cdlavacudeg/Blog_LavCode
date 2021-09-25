from django.db import models
from django.db.models.fields import CharField, DateField, EmailField
from django.core.validators import EmailValidator, validate_email

# Modelo Newsletter.
class Subscribers(models.Model):
    email=EmailField(validators=[validate_email],null=False,blank=False)
    fecha=DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name='Suscriptor'
        verbose_name_plural='Subscriptores'

class Mail(models.Model):
    titulo=CharField(max_length=250,null=True)
    message=models.TextField(null=True)

    def __str__(self):
        return self.titulo




