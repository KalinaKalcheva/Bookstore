from rest_framework import serializers
from .models import Author, Book

class AuthoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  
        fields = ['id', 'first_name', 'last_name']
    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  
        fields = ['id', 'title', 'author', 'genre', 'stock', 'price']