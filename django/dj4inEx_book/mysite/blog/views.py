"""This module for views in this app."""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm
from django.views.decorators.http import require_POST


class PostListView(ListView):
    """View post_list def in class."""

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


# def post_list(request) -> HttpResponse:
#     """View for all published posts."""
#     post_list = Post.published.all()
#     pg = Paginator(post_list, 3)
#     page_number = request.GET.get("page", 1)
#     try:
#         posts = pg.page(page_number)
#     except EmptyPage:
#         posts = pg.page(pg.num_pages)
#     except PageNotAnInteger:
#         posts = pg.page(1)
#     context: dict = {"posts": posts}
#     return render(request, "blog/post/list.html", context=context)


def post_detail(request, year, month, day, post) -> HttpResponse:
    """View for 1 post on this id."""
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    context: dict = {"post": post}

    return render(request, "blog/post/detail.html", context=context)


@require_POST
def post_comment(request, post_id) -> HttpResponse:
    """View for 1 comment in post."""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    form = CommentForm(data=request.Post)
    comment = None
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(
        request,
        "blog/post/comment.html",
        {"post": post, "form": form, "comment": comment},
    )
