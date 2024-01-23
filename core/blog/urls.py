from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path("get-blog/<id>",get_blog,name='get_blog'),
    path("login/",login_attempt,name='login'),
    path('register/',register_attempt,name='register'),
    path('show-all-blogs/',show_all_blogs,name='show_all_blogs'),
    path('create-blogs/',create_blogs,name='create_blogs'),
    path('update-blogs/<id>',update_blogs,name='update_blogs'),
    path('delete-blog/<id>/',delete_blog,name='delete_blog'),
    path('logout/',logout_attempt,name='logout'),
]