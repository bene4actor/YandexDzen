from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.posts.models import Post
from apps.ratings.models import PostRating
from apps.ratings.serializers import PostRatingSerializer


class PostRatingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        data = request.data
        data['post'] = post.id
        data['user'] = request.user.id
        serializer = PostRatingSerializer(data=data)

        if serializer.is_valid():
            PostRating.objects.update_or_create(
                post=post, user=request.user, defaults={'rating': data['rating']}
            )
            return Response({"message": "Rating added/updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
