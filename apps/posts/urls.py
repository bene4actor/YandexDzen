from django.contrib import admin
from django.urls import path

from .views import PostAddView, PostDetailView, PostListView

urlpatterns = [
    path("post/", PostListView.as_view(), name='post'),
    path("post_add/", PostAddView.as_view(), name='post_add'),
    path("post/<int:post_id>/", PostDetailView.as_view(), name='token_obtain_pair'),
]