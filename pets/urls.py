from django.urls import path, include
from .views import CreateUserView, LoginView, VerifyUserView, UserPetsView, PetViewSet, PostList, PostViewSet, CommentViewSet, FollowingViewSet, LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'pets', PetViewSet, basename='pets')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'following', FollowingViewSet, basename='following')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/verify/', VerifyUserView.as_view(), name='verify_user'),
    path('user/pets/', UserPetsView.as_view(), name='user-pets'),  # New URL pattern
    path('pet/<int:pet_id>/posts/', PostList.as_view(), name='pet_posts'),
    path('', include(router.urls)),  # Include the router.urls for the other views
]