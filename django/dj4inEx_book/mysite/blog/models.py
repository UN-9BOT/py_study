"""This module for standart models this app."""
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Index,
    Model,
    SlugField,
    TextChoices,
    TextField,
)
from django.contrib.auth.models import User
from django.utils import timezone


class Post(Model):
    """The model for posts in blog."""

    class Status(TextChoices):
        """For statuses in post."""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title: CharField = CharField(max_length=250)
    slug: SlugField = SlugField(max_length=250)
    author: ForeignKey = ForeignKey(
        User, on_delete=CASCADE, related_name="blog_posts")
    body: TextField = TextField(max_length=250)
    publish: DateTimeField = DateTimeField(default=timezone.now)
    created: DateTimeField = DateTimeField(auto_now_add=True)
    updated: DateTimeField = DateTimeField(auto_now=True)
    status: CharField = CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT)

    class Meta:
        """Metadata for db."""

        ordering = ["-publish"]
        indexes = [Index(fields=["-publish"])]

    def __str__(self) -> str:
        """Overload literal this model."""
        return self.title
