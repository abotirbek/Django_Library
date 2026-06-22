from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'library/home.html',{'books':books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request,'library/create.html',{'form':form})

def read_book(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,'library/read.html',{'book':book})

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', book.title)
        image = request.FILES.get('image', book.image)
        author = request.POST.get('author', book.author)
        isbn = request.POST.get('isbn', book.isbn)
        publisher = request.POST.get('publisher', book.publisher)
        publication_date = request.POST.get('publication_date', book.publication_date)
        pages = request.POST.get('pages', book.pages)
        description = request.POST.get('description', book.description)
        updated_at = models.DateTimeField(auto_now=True)
        if all([title, image, author, isbn, publisher, publication_date, pages, description]):
            book.title=title
            book.image=image
            book.author=author
            book.isbn=isbn
            book.publisher=publisher
            book.publication_date=str(publication_date)
            book.pages=pages
            book.description=str(description)
            book.save()
            return redirect('home')
    return render(request, 'library/update.html',{'book':book})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    else: return render(request,'library/delete.html',{'book':book})