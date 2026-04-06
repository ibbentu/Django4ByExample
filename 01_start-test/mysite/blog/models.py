from django.db import models
from django.utils import timezone

class Post(models.Model):
    # status
    class Status(models.Textchoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    # model
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # datetime
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # order
        ordering = ['-publish']

        # index
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title