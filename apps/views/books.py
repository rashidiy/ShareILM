from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from accounts.mixins import LoginAndVerificationRequiredMixin
from apps.forms import BookForm
from apps.models import Book, Category


class AllBooksListView(ListView):
    template_name = 'booksaw/all_books.html'
    queryset = Book.objects.all()
    paginator_class = Paginator(object_list=queryset, per_page=100)

    extra_context = {
        'categories': Category.objects.all(),
    }


class BookCreateView(LoginAndVerificationRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'booksaw/book_create.html'
    success_url = reverse_lazy('apps:my_books')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.owner = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class MyBooksListView(LoginAndVerificationRequiredMixin, ListView):
    template_name = 'booksaw/my_books.html'

    def get_queryset(self):
        return self.request.user.books.all()


class BookDeleteView(LoginAndVerificationRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('apps:my_books')
    template_name = 'booksaw/confirm_book_delete.html'

    def dispatch(self, request, *args, **kwargs):
        book = self.get_object()
        if book.owner != request.user:
            raise PermissionDenied("You do not have permission to delete this book.")
        return super().dispatch(request, *args, **kwargs)
