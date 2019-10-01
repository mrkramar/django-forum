from django.contrib import admin
from django.urls import path

from .views import (
    TopicCreateView,
    TopicListView,
    TopicDetailView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', TopicListView.as_view(), name='forum-index'),
    path('topic/add/', TopicCreateView.as_view(), name='topic-add'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),

    path('topic/<int:pk>/newpost/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
