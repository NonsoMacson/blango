from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.models import Post, Tag
from blog.api.serializers import PostSerializer, Userserializer, PostDetailSerializer, TagSerializer
from blango_auth.models import User


# class PostList(ListCreateAPIView):
#   queryset=Post.objects.all()
#   serializer_class=PostSerializer

# class PostDetail(RetrieveUpdateDestroyAPIView):
#   permission_classes=[AuthorModifyOrReadOnly | IsAdminUserForObject]
#   queryset=Post.objects.all()
#   serializer_class=PostDetailSerializer

class UserDetail(RetrieveAPIView):
  queryset=User.objects.all()
  lookup_field="email"
  serializer_class=Userserializer

class TagViewSet(ModelViewSet):
  queryset=Tag.objects.all()
  serializer_class=TagSerializer

  @action(methods=["get"], detail=True, name="Posts with this tag")
  def posts(self, request, pk=None):
    tag=self.get_object()
    post_serializer=PostSerializer(tag.posts, many=True, context={"request":request})
    return Response(post_serializer.data)

class PostViewSet(ModelViewSet):
  permission_classes=[AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset=Post.objects.all()

  def get_serializer_class(self):
    if self.action in ("list", "create"):
      return PostSerializer
    return PostDetailSerializer
