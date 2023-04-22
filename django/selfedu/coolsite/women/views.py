"""This module for all views in app women."""
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from .models import Women

menu: list[str] = ["Num", "Str", "List"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html',
                  {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request) -> HttpResponse:
    """Page about."""
    return render(request, "women/about.html",
                  {"menu": menu, "title": "about"})
