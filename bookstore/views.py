from django.http import JsonResponse
from .models import Author, Book
from .serializers import AuthoorSerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def AuthorList(request):
    # get all authors
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthoorSerializer(authors, many = True)
        return Response(serializer.data)

    # create a new author
    elif request.method == 'POST':
        serializer = AuthoorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def BooksList(request):
    # get all authors
    books = Book.objects.all()

    title = request.GET.get('title')
    author = request.GET.get('author')
    genre = request.GET.get('genre')

    if title:
        books = books.filter(title__icontains=title)

    if author:
        books = books.filter(author__last_name__icontains=author)

    if genre:
        books = books.filter(genre=genre)


    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def BookDetail(request, id):

    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

