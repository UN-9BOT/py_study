"""Views for the application."""
from django.db.models import SlugField
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
# from django.shortcuts import render


def quiz(reuqest: HttpRequest) -> HttpResponse:
    """Hello page."""
    return HttpResponse("Страница приложения quiz.".encode())


def trash(reuqest: HttpRequest, trash: SlugField) -> HttpResponse:
    """Trash page."""
    return HttpResponse(f"<h1>trash </h1>{trash}".encode())


def page_not_found(request: HttpRequest,
                   exception: Exception) -> HttpResponseNotFound:
    """Page 404."""
    return HttpResponseNotFound("<h1>Page not found</h1>".encode())
