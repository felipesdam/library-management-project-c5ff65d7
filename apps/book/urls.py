from django.urls import path
from apps.book.interfaces.views import BookListView, BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("<str:pk>/", BookDetailView.as_view(), name="book-detail"),
]
