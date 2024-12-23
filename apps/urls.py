from django.urls import path
from apps.views import HomeTemplateView, AllBooksListView, BookCreateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('books/all/', AllBooksListView.as_view(), name='all_books'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
]
