from rest_framework import serializers

from apps.ratings.models import PostRating


class PostRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostRating
        fields = ['id', 'post', 'user', 'rating']
