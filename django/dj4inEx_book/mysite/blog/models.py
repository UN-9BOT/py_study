"""This module for standart models this app."""
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Index,
    Manager,
    Model,
    QuerySet,
    SlugField,
    TextChoices,
    TextField,
)
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(Manager):
    """Manager for published post."""

    def get_queryset(self) -> QuerySet:
        """Overload."""
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(Model):
    """The model for posts in blog."""

    objects: Manager = Manager()
    published: PublishedManager = PublishedManager()

    class Status(TextChoices):
        """For statuses in post."""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title: CharField = CharField(max_length=250)
    slug: SlugField = SlugField(max_length=250, unique_for_date='publish')
    author: ForeignKey = ForeignKey(
        User, on_delete=CASCADE, related_name="blog_posts")
    body: TextField = TextField(max_length=250)
    publish: DateTimeField = DateTimeField(default=timezone.now)
    created: DateTimeField = DateTimeField(auto_now_add=True)
    updated: DateTimeField = DateTimeField(auto_now=True)
    status: CharField = CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    class Meta:
        """Metadata for db."""

        ordering = ["-publish"]
        indexes = [Index(fields=["-publish"])]

    def __str__(self) -> str:
        """Overload literal this model."""
        return self.title

    def get_absolute_url(self):
        """Resolve."""
        return reverse("blog:post_detail", args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])
