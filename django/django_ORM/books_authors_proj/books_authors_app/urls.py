from django.urls import path
from .views import index, createBook, newAuthor,addAuthor, createAuthor, showBook, showAuthor

urlpatterns = [
    path('', index, name='index'),
    path('createBook', createBook, name = 'createBook'),
    path('authors', newAuthor, name = 'newAuthor'),
    path('addAuthor', addAuthor, name = 'addAuthor'),
    path('createAuthor', createAuthor, name = 'createAuthor'),    
    path('books/<int: bookId>', showBook, name = 'showBook'),
    path('authors/<int: authorId>', showAuthor, name = 'showAuthor'),
]