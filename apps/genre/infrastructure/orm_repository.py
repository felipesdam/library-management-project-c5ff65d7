class GenreORMRepository:
    def save(self, instance):
        instance.save()

    def get_by_id(self, pk):
        return Genre.objects.get(pk=pk)
