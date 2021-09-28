from django import urls
from django.urls import path
from . import views


app_name='blog'
urlpatterns=[
     path('',views.HomeView.as_view(),name='all'),
     path('post/<slug:str>', views.PostDetailView.as_view(), name='post_detail'),
]