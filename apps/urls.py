from django.urls import path
from apps.views import HomeTemplateView, AllBooksListView, BookCreateView, MyBooksListView, BookDeleteView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('books/all/', AllBooksListView.as_view(), name='all_books'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/my_books/', MyBooksListView.as_view(), name='my_books'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
]
