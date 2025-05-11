from rest_framework import viewsets
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='authors__name', lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains') 
    edition = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['author', 'name', 'edition', 'publication_year']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
