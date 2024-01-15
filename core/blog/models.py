from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.Category_name
class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    banner_image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    