from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from blog.models import Post
from blog.api.serializers import PostSerializer


class PostList(ListCreateAPIView):
  queryset=Post.objects.all()
  serializer_class=PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
  queryset=Post.objects.all()
  serializer_class=PostSerializer