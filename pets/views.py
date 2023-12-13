from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet, Post, Comment, Following, Like
from .serializers import UserSerializer, PetSerializer, PostSerializer, FollowingSerializer, CommentSerializer, LikeSerializer 
from rest_framework_simplejwt.tokens import RefreshToken

# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })

# User Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class VerifyUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)  # Fetch user profile
        refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })


class IsPetOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of the associated pet to edit the post.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the associated pet.
        return obj.pet.owner == request.user

class UserPetsView(generics.ListAPIView):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve all pets associated with the currently authenticated user
        return Pet.objects.filter(owner=self.request.user)
        
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Require authentication and ownership for update and delete operations
            permission_classes = [permissions.IsAuthenticated, IsPetOwnerOrReadOnly]
        elif self.request.method == 'POST':
            # Require authentication for creating a new post
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Allow any access for other request methods (GET, POST)
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FollowingViewSet(viewsets.ModelViewSet): 
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

class LikeViewSet(viewsets.ModelViewSet): 
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


# Post Views (with protected POST route; requires token in header)
class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        pet_id = self.kwargs.get('pet_id')
        queryset = Post.objects.filter(pet=pet_id)
        return queryset
    
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]  

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            if user != request.user and not request.user.is_superuser:
                return Response({'error': 'You do not have permission to delete this user.'}, status=status.HTTP_403_FORBIDDEN)
            
            Pet.objects.filter(owner=user).delete()
            user.delete()

            return Response({'message': 'User and associated pets deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

