from django.shortcuts import render, redirect
from .models import Book, Authors

def index(request):
    books = Book.objects.all()
    context = {
        "books":books
    }
    return render(request, 'book.html', context)


def createBook(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'], description=request.POST['description'])
        return redirect('/')
    return redirect('/')



def showBook(request, bookId):
    thisBook = Book.objects.get(id=bookId)
    context = {
        "thisBook" : thisBook
    }
    return render(request,'showBook.html', context)
    
def addAuthor(request):
    bookId = request.POST['bookId']
    authorId = request.POST['authorId']
    thisBook = Book.objects.get(id=bookId)
    thisAuthor = Authors.objects.get(id=authorId)
    thisBook.myAuthors.add(thisAuthor)
    return redirect(f"/showBook/{bookId}")


def newAuthor(request):
    pass


def createAuthor(request):
    pass


def showAuthor(request):
    pass



# Create your views here.
