from django.contrib import admin
from .models import Author,Book

class Authors(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name',)
    list_per_page = 10
    search_fields = ('name',)

admin.site.register(Author,Authors)

class Books(admin.ModelAdmin):
    list_display = ('id','name','publication_year')
    list_display_links = ('id','name','publication_year',)
    list_per_page = 10
    search_fields = ('name','publication_year',)

admin.site.register(Book,Books)