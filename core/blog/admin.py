from django.contrib import admin
from .models import *
# Register your models here.
class Blogadmin(admin.ModelAdmin):
    list_display = ['title','category','user','created_at']
admin.site.register(Category)
admin.site.register(Blog, Blogadmin)