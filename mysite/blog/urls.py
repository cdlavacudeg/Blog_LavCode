from django import urls
from django.urls import path
from . import views
from home.views import HomeView

app_name='blog'
urlpatterns=[
     path('',HomeView.as_view(),name='all'),
     path('post/<slug:str>', views.PostDetailView.as_view(), name='post_detail'),
]