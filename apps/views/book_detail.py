# views.py
from django.shortcuts import render, get_object_or_404
from .books import Book
from django.shortcuts import redirect
from apps.models.cart import Cart,CartItem

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'booksaw/book_detail.html', {'book': book})


def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not item_created:
        cart_item.quantity += 1

    cart_item.save()

    return redirect('cart_detail')


