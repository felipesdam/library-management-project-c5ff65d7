class BookORMRepository:
    def save(self, instance):
        instance.save()

    def get_by_id(self, pk):
        return Book.objects.get(pk=pk)
