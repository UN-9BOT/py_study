# Generated by Django 4.2 on 2023-04-22 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("text", models.CharField(max_length=1024)),
                ("quiz", models.ManyToManyField(to="app.quiz")),
            ],
        ),
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("text", models.CharField(max_length=255)),
                ("is_correct", models.BooleanField()),
                ("question", models.ManyToManyField(to="app.question")),
            ],
        ),
        migrations.CreateModel(
            name="Answers",
            fields=[
                (
                    "quiz_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("answers", models.ManyToManyField(to="app.quiz")),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "question_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("text", models.CharField(max_length=1024)),
                ("choices", models.ManyToManyField(to="app.answers")),
            ],
        ),
    ]
