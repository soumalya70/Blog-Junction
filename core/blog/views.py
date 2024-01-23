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
    context={"blogs":Blog.objects.filter(user=request.user)}
    return render (request,'show_all_blogs.html',context)
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

def update_blogs(request,id):
    context={'categories': Category.objects.all()}
    try:
        if request.method =="POST":
            form=BlogForm(request.POST)
            category= request.POST.get('category')
            title=request.POST.get('title')
            banner_image=request.FILES['banner_image']
            if form.is_valid():
                content=form.cleaned_data['content']
                blog_obj=Blog.objects.get(id=id)
            
                blog_obj.title=title
                blog_obj.content=content
                blog_obj.category=Category.objects.get(id=category)
                if banner_image:
                    blog_obj.banner_image=banner_image
                blog_obj.save()
                messages.success(request,"Blog Updated successfully")
                return redirect('/create-blogs/')
        blog_obj = Blog.objects.get(id=id)
        if blog_obj.user != request.user:
            return redirect('/')
        initial_dict={'content': blog_obj.content}
        form=BlogForm(initial=initial_dict)
        context['form']=form
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)
    return render(request,'update_blogs.html', context)
def delete_blog(request,id):
    blog_obj = Blog.objects.get(id=id)
    if  blog_obj.user!=request.user:
        return redirect('/')
    blog_obj.delete()
    return redirect('/show-all-blogs/')
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