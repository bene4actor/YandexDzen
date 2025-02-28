from rest_framework import serializers

from apps.posts.models import Post
from apps.ratings.models import PostRating


class PostSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['text', 'created_at', 'user', 'average_rating']

    def get_average_rating(self, obj):
        ratings = PostRating.objects.filter(post=obj)
        if ratings:
            return sum([rating.rating for rating in ratings])/len(ratings)
        return 0

