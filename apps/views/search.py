from django.shortcuts import render
from .books import Book

def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(
            title__icontains=query
        ) | Book.objects.filter(
            author__name__icontains=query
        ) | Book.objects.filter(
            category__name__icontains=query
        )
    else:
        books = Book.objects.all()

    return render(request, 'booksaw/search_results.html', {'books': books})
