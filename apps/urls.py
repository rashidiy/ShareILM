from django.urls import path
from .views import AllBooksListView, BookCreateView, MyBooksListView, BookDeleteView,search_books,book_detail
from .views.book_detail import add_to_cart

urlpatterns = [
    path('all/', AllBooksListView.as_view(), name='all_books'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('my_books/', MyBooksListView.as_view(), name='my_books'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('search/', search_books, name='search_books'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    # path('book/<int:book_id>/', book_detail, name='books_detail'),
]
