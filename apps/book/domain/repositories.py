from abc import ABC, abstractmethod

class BookRepositoryInterface(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def retrieve(self, pk):
        pass

    @abstractmethod
    def update(self, pk, data):
        pass

    @abstractmethod
    def delete(self, pk):
        pass
