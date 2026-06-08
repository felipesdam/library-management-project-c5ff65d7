class AuthorORMRepository:
    def save(self, instance):
        instance.save()

    def get_by_id(self, pk):
        return Author.objects.get(pk=pk)
