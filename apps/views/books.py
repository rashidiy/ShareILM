from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, CreateView, DeleteView, FormView, DetailView

from accounts.mixins import LoginAndVerificationRequiredMixin
from apps.forms import BookForm, ReviewCreateForm
from apps.models import Book, Category, Review


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

class BookDetailView(LoginAndVerificationRequiredMixin,FormView, DetailView):
    model = Book
    template_name = 'booksaw/book_detail.html'
    context_object_name = 'book'
    form_class = ReviewCreateForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        context['categories'] = book.category.all()
        context['reviews'] = Review.objects.filter(book=book).order_by('-created_at')
        return context
    def form_valid(self, form):
        book = self.get_object()
        review = form.save(commit=False)
        review.book = book
        review.user = self.request.user
        review.save()
        return HttpResponseRedirect(self.request.path_info)

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.pk})
