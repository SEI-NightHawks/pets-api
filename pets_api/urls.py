"""
URL configuration for pets_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')).
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pets.urls'))
]

# from django.urls import path
# from .views import CreateUserView, LoginView, PetList, PetDetail, PostDetail, PostList, FollowingDetail, FollowingList, CommentDetail, CommentList, LikeDetail, LikeList 

# urlpatterns = [
#   # User routes
#   path('users/register/', CreateUserView.as_view(), name='register'),
#   path('users/login/', LoginView.as_view(), name='login'),

#   # Other routes
# #   path('pets/', PetList.as_view(), name='pet-list'),  # List all blogs and create a blog
# #   path('pets/<int:pk>/', PetDetail.as_view(), name='pet-detail'),  # Retrieve, update, and delete a specific blog

#   path('posts/', PostList.as_view(), name='post-list'),  # List all comments and create a comment
#   path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Update and delete a specific comment
  
#   path('followings/', FollowingList.as_view(), name='following-list'),  # List all comments and create a comment
#   path('followings/<int:pk>/', FollowingDetail.as_view(), name='following-detail'),  # Update and delete a specific comment
  
#   path('comments/', CommentList.as_view(), name='comment-list'),  # List all comments and create a comment
#   path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),  # Update and delete a specific comment
  
#   path('likes/', LikeList.as_view(), name='like-list'),  # List all comments and create a comment
#   path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),  # Update and delete a specific comment
# ]
#
