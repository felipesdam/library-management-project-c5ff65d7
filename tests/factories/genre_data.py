import factory
from apps.genre.domain.models import Genre
from core.utils.fake import generate_random_value

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    # Campos simples
    id = generate_random_value("UUIDField")
    name = generate_random_value("CharField")

    # OneToOne or ForeignKey relationships

    # ManyToMany relationships
