"""Core models."""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    """Manager for objects with Published status."""

    def get_queryset(self) -> models.QuerySet:
        """Overload."""
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class CommentrueManager(models.Manager):
    """Manager for comment with status True."""

    def get_queryset(self) -> models.QuerySet:
        """Overload."""
        return super().get_queryset().filter(active=True)


class Post(models.Model):
    """Model for post in blog."""

    class Status(models.TextChoices):
        """Field status: Draft/Published."""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title: models.CharField = models.CharField(max_length=250)
    author: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    slug: models.SlugField = models.SlugField(
        max_length=250, unique_for_date='publish')
    body: models.TextField = models.TextField()
    publish: models.DateTimeField = models.DateTimeField(default=timezone.now)
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField = models.DateTimeField(auto_now=True)
    status: models.CharField = models.CharField(max_length=2,
                                                choices=Status.choices,
                                                default=Status.DRAFT)
    objects: models.Manager = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        """Overload."""
        return self.title

    class Meta:
        """Meta info for db."""

        ordering = ["-publish"]
        indexes = [models.Index(fields=['-publish'])]
        db_table = "post"

    def get_absolute_url(self) -> str:
        """Resover for url."""
        return reverse("core:post_detail", args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])


class Comment(models.Model):
    """View for comment under the post."""

    post: models.ForeignKey = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name: models.CharField = models.CharField(max_length=80)
    body: models.TextField = models.TextField()
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField = models.DateTimeField(auto_now=True)
    active: models.BooleanField = models.BooleanField(default=True)
    commentrue = CommentrueManager()

    class Meta:
        """Metadata for db."""

        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]

    def __str__(self) -> str:
        """Overload."""
        return f"Comment by {self.name} on {self.post}"
