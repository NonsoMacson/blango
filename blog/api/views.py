from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.models import Post
from blog.api.serializers import PostSerializer, Userserializer, PostDetailSerializer
from blango_auth.models import User


class PostList(ListCreateAPIView):
  queryset=Post.objects.all()
  serializer_class=PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
  permission_classes=[AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset=Post.objects.all()
  serializer_class=PostDetailSerializer

class UserDetail(RetrieveAPIView):
  queryset=User.objects.all()
  lookup_field="email"
  serializer_class=Userserializer