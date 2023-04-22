"""This module for creating forms."""
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for comment in post."""

    class Meta:
        """Metadata."""

        model = Comment
        field = ["name", "email", "body"]


# class EmailPostForm(forms.Form):
#     """First form."""

#     name: forms.CharField = forms.CharField(max_length=25)
#     email: forms.EmailField = forms.EmailField()
#     to: forms.EmailField = forms.EmailField()
#     comments = forms.CharField(required=False, widget=forms.Textarea)
