from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Add other fields as needed

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

class Following(models.Model):
    follower = models.ForeignKey('auth.User', related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey('auth.User', related_name='followers', on_delete=models.CASCADE)
    # Add other fields as needed

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # Add other fields as needed

class Like(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed
