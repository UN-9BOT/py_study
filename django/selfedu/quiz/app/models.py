"""Module for defining the models for the quiz app."""
from uuid import uuid4
from django.db.models import CASCADE, ForeignKey, ManyToManyField, Model, TextField
from django.db.models.fields import BooleanField, CharField


class Quiz(Model):
    """Model for storing the Quiz object in the database."""

    uuid: CharField = CharField(
        max_length=36,
        primary_key=True,
        editable=False)
    title: CharField = CharField(max_length=255)


class Question(Model):
    """Model for storing the Question object in the database."""

    uuid: CharField = CharField(
        max_length=36,
        primary_key=True,
        editable=False)
    text: TextField = TextField(max_length=1024)
    quiz: ForeignKey = ForeignKey(
        Quiz, on_delete=CASCADE, related_name="questions")


class Choice(Model):
    """Model for storing the Choice object in the database."""

    uuid: CharField = CharField(
        max_length=36,
        primary_key=True,
        editable=False)
    text: TextField = TextField(max_length=255)
    is_correct: BooleanField = BooleanField(default=False)
    question: ForeignKey = ForeignKey(
        Question, on_delete=CASCADE, related_name="choices"
    )


class Answer(Model):
    """Model for storing the Answer object in the database."""

    uuid: CharField = CharField(
        max_length=36,
        primary_key=True,
        editable=False)
    question: ForeignKey = ForeignKey(
        Question, on_delete=CASCADE, related_name="answers"
    )
    choice: ForeignKey = ForeignKey(Choice, on_delete=CASCADE)


class Answers(Model):
    """Model for storing the Answers object in the database."""

    quiz: ForeignKey = ForeignKey(
        Quiz, on_delete=CASCADE, related_name="answers", default=None
    )
    answers: ManyToManyField = ManyToManyField(Answer)
