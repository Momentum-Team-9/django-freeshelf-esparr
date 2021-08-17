from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})