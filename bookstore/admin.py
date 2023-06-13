from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models.query import QuerySet
from .models import Author, Book



class InStockFilter(SimpleListFilter):

    title = 'Stock'
    parameter_name = 'stock'

    def lookups(self, request, model_admin):
        return [
            ('in_stock', 'In Stock'),
            ('out_of_stock', 'Out of Stock'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'in_stock':
            return queryset.filter(stock__gt=0)
        if self.value() == 'out_of_stock':
            return queryset.filter(stock=0)

class BookAdminSite(admin.ModelAdmin):
    model = Book
    fields = []
    list_display = ['title', 'author', 'genre','stock', 'price']
    actions = ['books_sale']
    list_filter = ('author','genre', InStockFilter)

    def books_sale(self, request, queryset):
        for book in queryset:
            book.price-= book.price*0.2
            book.save()



admin.site.register(Author)
admin.site.register(Book, BookAdminSite)
