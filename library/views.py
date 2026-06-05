from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'library/home.html',{'books':books})

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        publisher = request.POST.get('publisher')
        publication_date = request.POST.get('publication_date')
        pages = request.POST.get('pages')
        description = request.POST.get('description')
        if title and author and isbn and publisher and publication_date and pages and description:
            Book.objects.create(
                title = title,
                author = author,
                isbn = isbn,
                publisher = publisher,
                publication_date = publication_date,
                pages = pages,
                description = description
            )
            return redirect('create')
    else: return render(request,'library/create.html')

def read_book(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,'library/read.html',{'book':book})

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', book.title)
        author = request.POST.get('author', book.author)
        isbn = request.POST.get('isbn', book.isbn)
        publisher = request.POST.get('publisher', book.publisher)
        publication_date = request.POST.get('publication_date', book.publication_date)
        pages = request.POST.get('pages', book.pages)
        description = request.POST.get('description', book.description)
        updated_at = request.POST.get('updated_at', book.updated_at)
        if title and author and isbn and publisher and publication_date and pages and description and updated_at:
            book.title=title
            book.author=author
            book.isbn=isbn
            book.publisher=publisher
            book.publication_date=str(publication_date)
            book.pages=pages
            book.description=str(description)
            book.updated_at = str(updated_at)
            book.save()
            return redirect('home')
    else: return render(request, 'library/update.html',{'book':book})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    else: return render(request,'library/delete.html',{'book':book})