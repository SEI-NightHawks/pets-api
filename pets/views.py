from rest_framework import viewsets
from .serializers import PetSerializer, PostSerializer, FollowingSerializer, CommentSerializer, LikeSerializer 
from .models import Pet, Post, Following, Comment, Like
# Create your views here.

class PetViewSet(viewsets.ModelViewSet): 
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FollowingViewSet(viewsets.ModelViewSet): 
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet): 
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


