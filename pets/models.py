from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('not specified', 'not specified'),
)

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.URLField(max_length=600)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, blank=True)  

    def __str__(self):
        return f'{self.name} - {self.breed}'

class Post(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='posts') 
    content = models.TextField()
    post_image = models.URLField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pet.name} - {self.content}'

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pet}- {self.comment}'

class Following(models.Model):
    follower = models.ForeignKey(Pet, related_name='following', on_delete=models.CASCADE)
    followed_pet = models.ForeignKey(Pet, related_name='followers', on_delete=models.CASCADE, null=True, blank=True)

class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    