from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.models import Post
from blog.api.serializers import PostSerializer


class PostList(ListCreateAPIView):
  queryset=Post.objects.all()
  serializer_class=PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
  permission_classes=[AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset=Post.objects.all()
  serializer_class=PostSerializer