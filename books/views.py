from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, User, Category
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('list_books')
    return render(request, 'books/index.html', {'users': users})

@login_required
def list_books(request, ):
    ordered_books = Book.objects.order_by('-created_at')
    return render(request, 'books/list_books.html', {'books': ordered_books})

@login_required
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "books/add_book.html", {"form": form})

@login_required
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    categories = Book.categories
    return render(
        request, "books/view_book.html",
        {"book": book, "pk": pk, }
    )

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else: 
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')

    return render(request, "books/delete_book.html",
        {"book": book})

@login_required
def show_category(request, slug):
    category = str(get_object_or_404(Category, slug=slug))
    books = Book.objects.all()

    return render(request, "books/view_category.html", {"category": category, "books": books})


