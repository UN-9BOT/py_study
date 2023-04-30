"""For admin panel."""
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Field in left table for edit."""

    list_display = ["title", "slug", "author", "publish", "status"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
