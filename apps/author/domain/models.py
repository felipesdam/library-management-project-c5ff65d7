from django.db import models
from django.db.models import Q
import uuid

class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    mentor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return " | ".join([
            str(self.id),
            str(self.name),
        ])

    class Meta:
        db_table = "authors"
        ordering = [
            "created_at",
        ]
