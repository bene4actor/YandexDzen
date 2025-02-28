from django.db import models

from apps.posts.models import Post
from apps.users.models import User


class PostRating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"Rating for {self.post.text[:50]} by {self.user.username}"