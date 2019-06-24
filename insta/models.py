from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    pic=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=30)
    userId=models.IntegerField()


    


class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30)
    likes=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    userId=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


   

class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.IntegerField()


class Followers(models.Model):
    user=models.CharField(max_length=30)
    insta=models.CharField(default='',max_length=30)
    user_id=models.IntegerField()


    
