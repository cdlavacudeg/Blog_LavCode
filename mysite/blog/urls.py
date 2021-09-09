from django import urls
from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
     path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]