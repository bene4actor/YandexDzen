from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.comments.models import Comment
from apps.comments.serializers import PostCommentSerializer
from apps.posts.models import Post



class AddCommentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        data = request.data
        data['post'] = post.id
        if request.user.is_authenticated:
            data['user'] = request.user.id
        else:
            data['author_name'] = request.data.get('author_name', "Anonymous")
        serializer = PostCommentSerializer(data=data)

        if serializer.is_valid():
            comment = serializer.save()
            return Response(PostCommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(generics.ListAPIView):
    serializer_class = PostCommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)


class EditCommentView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostCommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            comment = serializer.save()
            return Response(PostCommentSerializer(comment).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCommentView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response({"message": "Comment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)