from apps.book.domain.repositories import BookRepositoryInterface

class BookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def create(self, data):
        return self.repository.create(data)

    def list(self):
        return self.repository.list()

    def retrieve(self, pk):
        return self.repository.retrieve(pk)

    def update(self, pk, data):
        return self.repository.update(pk, data)

    def delete(self, pk):
        return self.repository.delete(pk)
