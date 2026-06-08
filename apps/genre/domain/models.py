from django.db import models
from django.db.models import Q
import uuid

class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(
        unique=True,
        max_length=80,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return " | ".join([
            str(self.id),
            str(self.name),
        ])

    class Meta:
        db_table = "genres"
        ordering = [
            "created_at",
        ]
