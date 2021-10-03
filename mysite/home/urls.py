from django import urls
from django.urls import path
from . import views

app_name='home'
urlpatterns=[
    path('',views.Home.as_view(),name='all'),
    path('sub',views.Subcripcion.as_view(),name='sub_ok')
]