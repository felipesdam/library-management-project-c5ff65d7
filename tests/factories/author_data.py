import factory
from apps.author.domain.models import Author
from core.utils.fake import generate_random_value
from tests.factories.Author_data import AuthorFactory

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    # Campos simples
    id = generate_random_value("UUIDField")
    name = generate_random_value("CharField")

    # OneToOne or ForeignKey relationships

    # ManyToMany relationships
