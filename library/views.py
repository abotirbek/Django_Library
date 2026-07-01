from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from accounts.permissions import checking_login, checking_admin


# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'library/home.html',{'books':books})

@checking_admin
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request,'library/create.html',{'form':form})

@checking_login
def read_book(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,'library/read.html',{'book':book})

@checking_admin
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/update.html',{'form':form})

@checking_admin
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    else: return render(request,'library/delete.html',{'book':book})