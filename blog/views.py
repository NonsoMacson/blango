from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm

import logging


logger=logging.getLogger(__name__)

# Create your views here.


def index(request):
  posts=Post.objects.filter(published_at__lte=timezone.now())
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


