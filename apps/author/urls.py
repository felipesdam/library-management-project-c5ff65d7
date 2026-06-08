from django.urls import path
from apps.author.interfaces.views import AuthorListView, AuthorDetailView

urlpatterns = [
    path("", AuthorListView.as_view(), name="author-list"),
    path("<str:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]
