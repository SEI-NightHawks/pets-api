from django.contrib import admin
from .models import Pet, Post, Following, Comment, Like
# Register your models here.

admin.site.register(Pet)
admin.site.register(Post)
admin.site.register(Following)
admin.site.register(Comment)
admin.site.register(Like)