"""This module for standart models this app."""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    """Manager for published post."""

    def get_queryset(self) -> models.QuerySet:
        """Overload."""
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """The model for posts in blog."""

    objects: models.Manager = models.Manager()
    published: PublishedManager = PublishedManager()

    class Status(models.TextChoices):
        """For statuses in post."""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title: models.CharField = models.CharField(max_length=250)
    slug: models.SlugField = models.SlugField(
        max_length=250, unique_for_date="publish"
    )
    author: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body: models.TextField = models.TextField(max_length=250)
    publish: models.DateTimeField = models.DateTimeField(default=timezone.now)
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField = models.DateTimeField(auto_now=True)
    status: models.CharField = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    class Meta:
        """Metadata for db."""

        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self) -> str:
        """Overload literal this model."""
        return self.title

    def get_absolute_url(self) -> str:
        """Resolve."""
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )


class Comment(models.Model):
    """The model for comments in post."""

    post: models.ForeignKey = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name: models.CharField = models.CharField(max_length=80)
    email: models.EmailField = models.EmailField()
    body: models.TextField = models.TextField()
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField = models.DateTimeField(auto_now=True)
    active: models.BooleanField = models.BooleanField()

    class Meta:
        """Metadata for db."""

        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]

    def __str__(self) -> str:
        """Overload."""
        return f"Comment by {self.name} on {self.post}"
