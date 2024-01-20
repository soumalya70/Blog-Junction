from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')
def login_attempt(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username)
        if not user_obj.exists():
            messages.success(request, "User not found")
            return redirect("/login/")
        user_obj=authenticate(username=username,password=password)
        if not user_obj:
            messages.success(request, "Invalid Credentials")
            return redirect("/login/")
        login(request, user_obj)
        return redirect("/")
            
    return render(request,'login_attempt.html')
def register_attempt(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username)
        if user_obj.exists():
            messages.success(request,"Username is taken")
            return redirect("/register/")
        user_obj=User.objects.filter(email=email)
        if user_obj.exists():
            messages.success(request,"Email is taken")
            return redirect("/register/")
        user_obj=User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,"Your account is created")
        return redirect("/login/")
    return render(request,"register_attempt.html")
        
    # return render(request,'register_attempt.html')
def show_all_blogs(request):
    return render (request,'show_all_blogs.html')
def create_blogs(request):
    context={'form': BlogForm, 'categories': Category.objects.all()}
    if request.method =="POST":
        form=BlogForm(request.POST)
        category= request.POST.get('category')
        title=request.POST.get('title')
        banner_image=request.FILES['banner_image']
        if form.is_valid():
            content=form.cleaned_data['content']
            Blog.objects.create(
                title=title, content=content, category=Category.objects.get(id=category),
                user=request.user,banner_image=banner_image)
            messages.success(request,"Blog created successfully")
            return redirect('/create-blogs/')
    return render(request,'create_blogs.html',context)

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

def logout_attempt(request):
    logout(request)
    return redirect('/')