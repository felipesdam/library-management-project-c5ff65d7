import factory
from apps.book.domain.models import Book
from core.utils.fake import generate_random_value
from tests.factories.Author_data import AuthorFactory
from tests.factories.Genre_data import GenreFactory

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    # Campos simples
    id = generate_random_value("UUIDField")
    title = generate_random_value("CharField")
    published = generate_random_value("BooleanField")

    # OneToOne or ForeignKey relationships
    genres = factory.SubFactory(GenreFactory)

    # ManyToMany relationships
    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.genres = extracted
        else:
            self.genres.add(GenreFactory())
