"""This module for all views in app women."""
from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    """Start page."""
    menu: list[str] = ["start"]
    context: dict = {"menu": menu}
    return render(request, "app/index.html", context=context)
