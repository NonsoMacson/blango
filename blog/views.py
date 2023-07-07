from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
#from django.views.decorators.cache import cache_page
#from django.views.decorators.vary import vary_on_cookie
import logging


logger=logging.getLogger(__name__)

# Create your views here.

#@cache_page(300)
#@vary_on_cookie
def index(request):
  #from django.http import HttpResponse
  #logger.info("The current user is %s", request.user)
  #return HttpResponse(str(request.user).encode("ascii"))
  
  posts=Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
  
  # posts = (
  #   Post.objects.filter(published_at__lte=timezone.now())
  #   .select_related("author")
  #   .defer("created_at", "modified_at")
  # )

  #   posts = (
  #     Post.objects.filter(published_at__lte=timezone.now())
  #     .select_related("author")
  #     .only("title", "summary", "content", "author", "published_at", "slug")
  
  # )
  logger.debug("Got %d posts", len(posts))
  return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, slug):
  post=get_object_or_404(Post, slug=slug)
  
  if request.user.is_active:
    if request.method=="POST":
      comment_form= CommentForm(request.POST)

      if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.creator=request.user
        comment.content_object=post
        comment.save()
        logger.info("created comment on Post %d for user %s", post.pk, request.user)
        return redirect(request.path_info)
    else:
        comment_form=CommentForm()
  else:
    comment_form=None

  return render(
     request, "blog/post-detail.html", {"post":post, "comment_form":comment_form}
     )


def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])