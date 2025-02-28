from django.conf import settings
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.posts.tasks import send_telegram_message


class PostAddView(APIView):

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            post = serializer.save(user=request.user)
            # Отправка сообщения в Telegram через Celery
            chat_id = request.user.telegram_chat_id
            message = f"Ваш пост '{post.text[:50]}...' опубликован!"
            send_telegram_message.delay(chat_id, message)  # Асинхронный вызов

            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, post_id):
        return get_object_or_404(Post, id=post_id)

    def get(self, request, post_id):
        post = self.get_object(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_post(self, request, post_id, partial=False):
        post = self.get_object(post_id)
        if request.user == post.user or request.user.is_staff:
            serializer = PostSerializer(post, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, post_id):
        return self.update_post(request, post_id, partial=False)

    def patch(self, request, post_id):
        return self.update_post(request, post_id, partial=True)

    def delete(self, request, post_id):
        post = self.get_object(post_id)
        if request.user == post.user or request.user.is_staff:
            post.delete()
            return Response({'message': "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

