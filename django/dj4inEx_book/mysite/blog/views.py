"""This module for views in this app."""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request) -> HttpResponse:
    """View for all published posts."""
    post_list = Post.published.all()
    pg = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = pg.page(page_number)
    except EmptyPage:
        posts = pg.page(pg.num_pages)
    except PageNotAnInteger:
        posts = pg.page(1)
    context: dict = {"posts": posts}
    return render(request, "blog/post/list.html", context=context)


def post_detail(request, year, month, day, post) -> HttpResponse:
    """View for 1 post on this id."""
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    context: dict = {"post": post}

    return render(request, "blog/post/detail.html", context=context)


