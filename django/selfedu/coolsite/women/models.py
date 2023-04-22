"""
This module contains the Women model that represents a woman's article.

Classes:
- Women: A model that represents a woman's article.

"""

from django.db.models import Model, DateTimeField, BooleanField
from django.db.models import CharField, TextField, ImageField


class Women(Model):
    """A model that represents a woman's article."""

    title: CharField = CharField(max_length=255, verbose_name="Заголовок")
    content: TextField = TextField(blank=True, verbose_name="Текст статьи")
    photo: ImageField = ImageField(
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Фото")
    time_create: DateTimeField = DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    time_update: DateTimeField = DateTimeField(
        auto_now=True, verbose_name="Время изменения"
    )
    is_published: BooleanField = BooleanField(verbose_name="Публикация")

    def __str__(self):
        """Overload str views."""
        return self.title
