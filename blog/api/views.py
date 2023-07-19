from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.models import Post, Tag
from blog.api.serializers import PostSerializer, Userserializer, PostDetailSerializer, TagSerializer
from blango_auth.models import User

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

from rest_framework.exceptions import PermissionDenied


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

  @method_decorator(cache_page(120))
  def get(self, *args, **kwargs):
    return super(UserDetail, self).get(*args, **kwargs)






class TagViewSet(ModelViewSet):
  queryset=Tag.objects.all()
  serializer_class=TagSerializer

  @action(methods=["get"], detail=True, name="Posts with this tag")
  def posts(self, request, pk=None):
    tag=self.get_object()
    post_serializer=PostSerializer(tag.posts, many=True, context={"request":request})
    return Response(post_serializer.data)

  
  @method_decorator(cache_page(300))
  def list(self, *args, **kwargs):
    return super(TagViewSet, self).list(*args, **kwargs)
    
  @method_decorator(cache_page(300))
  def retrieve(self, *args, **kwargs):
    return super(TagViewSet, self).retrieve(*args, **kwargs)





class PostViewSet(ModelViewSet):
  permission_classes=[AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset=Post.objects.all()

  def get_serializer_class(self):
    if self.action in ("list", "create"):
      return PostSerializer
    return PostDetailSerializer

  @method_decorator(cache_page(300))
  @method_decorator(vary_on_headers("Authorization"))
  @method_decorator(vary_on_cookie)
  @action(methods=['get'], detail=False, name="Posts by the logged in user")
  def mine(self, request):
    if request.user.is_anonymous:
      raise PermissionDenied("You must be logged in to which Posts are yours")
    posts=self.get_querset().filter(authro=request.user)
    serializer=PostSerializer(posts, many=true, context={"request":request})
    return Response(serializer.data)

  @method_decorator(cache_page(120))
  def list(self, *args, **kwargs):
    return super(PostViewSet, self).list(*args, **kwargs)


  

