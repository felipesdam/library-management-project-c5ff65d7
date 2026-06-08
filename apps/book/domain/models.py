from django.db import models
from django.db.models import Q
import uuid

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    title = models.CharField(
        unique=True,
        max_length=255,
    )
    published = models.BooleanField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    author = models.ForeignKey(
        "author.Author",
        on_delete=models.CASCADE,
        related_name='books',
    )
    genres = models.ManyToManyField(
        "genre.Genre",
        blank=True,
    )

    def __str__(self):
        return " | ".join([
            str(self.id),
            str(self.title),
            str(self.published),
        ])

    class Meta:
        db_table = "books"
        ordering = [
            "-title",
        ]
        indexes = [
            models.Index(
                fields=['title'],
                name='BookTitleIdx',
            ),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='UniqueBookAuthor',
                deferrable=models.Deferrable.DEFERRED,
            ),
            models.CheckConstraint(
                condition=Q(title__isnull=False),
                name='BookTitleRequired',
            ),
        ]
