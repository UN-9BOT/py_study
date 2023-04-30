"""Views for app -> core."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    """View for page with all posts."""
    post_list = Post.published.all()
    pg = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = pg.page(page_number)

    context = {"posts": posts}
    return render(request, "core/post/list.html", context=context)


def post_detail(request: HttpRequest, year, month, day, post) -> HttpResponse:
    """View for page with 1 post and full info about this post."""
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    context = {"post": post}
    return render(request, "core/post/detail.html", context=context)
