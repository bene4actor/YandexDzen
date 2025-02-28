from django.contrib import admin
from django.urls import path

from .views import AddCommentView, EditCommentView, DeleteCommentView, CommentListView

urlpatterns = [
    path("post/<int:post_id>/comment_add", AddCommentView.as_view(), name='add_comment'),
    path("post/<int:post_id>/comment", CommentListView.as_view(), name='comment'),
    path("comment/<int:comment_id>/edit", EditCommentView.as_view(), name="comment_edit"),
    path("comment/<int:comment_id>/delete", DeleteCommentView.as_view(), name='comment_delete')

]