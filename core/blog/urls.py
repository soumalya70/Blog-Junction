from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("get-blog/<id>",get_blog,name='get_blog'),
]