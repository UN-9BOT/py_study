"""Views for app -> core."""
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.decorators.http import require_POST

from .forms import CommentForm
from .models import Post, Comment


class PostListView(ListView):
    """View on based class."""

    model = Post
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'core/post/list.html'

    def get(self, request: HttpRequest, *args: str,
            **kwargs: int) -> HttpResponse:
        """For get query."""
        post_list = self.get_queryset()
        paginator = Paginator(post_list, self.paginate_by)
        page_number = request.GET.get('page', 1)
        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {"posts": posts}
        return render(request, self.template_name, context=context)


def post_detail(request: HttpRequest, year: int, month: int,
                day: int, post: Any) -> HttpResponse:
    """View for page with 1 post and full info about this post."""
    post_view: Post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    comments = Comment.commentrue.all()
    form = CommentForm()
    context = {"post": post_view,
               "comments": comments,
               "form": form}
    return render(request, "core/post/detail.html", context=context)


@require_POST
def post_comment(request: HttpRequest, post_id: int) -> HttpResponse:
    """View for comment under the post."""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {"post": post, "form": form, "comment": comment}
    return render(request, 'core/post/comment.html',
                  context=context)
