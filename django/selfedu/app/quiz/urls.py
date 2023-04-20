"""Url conf for Quiz app."""
from django.urls import path
from .views import quiz, trash


urlpatterns = [
    path("", quiz),
    path("trash/<slug:trash>/", trash)
]
