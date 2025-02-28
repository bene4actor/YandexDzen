from rest_framework import serializers

from apps.comments.models import Comment


class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'user', 'author_name', 'comment_text', 'created_date', 'post']
