from django.db import models

from apps.posts.models import Post
from apps.users.models import User


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    author_name = models.CharField(max_length=255, null=True, blank=True)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text[:50]
