"""For admin panel."""
from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Field in left table for edit."""

    list_display = ["title", "slug", "author", "publish", "status"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish"
    ordering = ["status", "publish"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Field for comments in admin panel."""

    list_display = ["name", "post", "created", "body", "active",]
    list_filter = ["active", "post", "name", "created", "updated"]
    search_fields = ["name", "body"]
    list_editable = ["active",]

