from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blogs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogss')
    blog_title = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    content = RichTextField(blank=True,null=True)
    topic = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to='p_images')

    def __str__(self):
        return self.blog_title

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    pro_pic = models.ImageField(upload_to='p_images')
    date_of_birth = models.DateField(null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    phone = models.CharField(max_length=14,default='+91-')

