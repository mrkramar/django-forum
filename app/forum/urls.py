from django.contrib import admin
from django.urls import path

from .views import (
    TopicListView,
    TopicDetailView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', TopicListView.as_view(), name='forum-index'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
