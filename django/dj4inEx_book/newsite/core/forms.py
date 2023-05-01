"""Forms in blog under the post."""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Form for comment."""

    class Meta:
        """Metadata for db."""

        model = Comment
        fields = ["name", "body"]

