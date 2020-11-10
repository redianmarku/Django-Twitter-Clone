from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    FollowsListView,
    FollowersListView,
    postpreference,
    post_list)
from .import views
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),
    path('post/<int:postid>/preference/<int:userpreference>', postpreference, name='postpreference'),
    path('l/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/posts', post_list)
]
