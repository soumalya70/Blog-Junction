from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')
def login_attempt(request):
    return render(request,'login_attempt.html')
def register_attempt(request):
    return render(request,'register_attempt.html')
def show_all_blogs(request):
    return render (request,'show_all_blogs.html')
def create_blogs(request):
    return render(request,'create_blogs.html')
def update_blogs(request):
    return render(request,'update_blogs.html')
def delete_blog(request,id):
    return redirect('/')
def get_blog(request,id):
    context={}
    try:
        blog_obj=Blog.objects.get(id=id)
        context['blog']=blog_obj
    except Exception as e:
        print(e)
        
    return render(request, 'detail_blog.html', context)