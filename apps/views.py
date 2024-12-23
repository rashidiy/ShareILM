from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from apps.forms import BookForm
from apps.models import Book, Category

"""
GENERIC VIEWS

TemplateView

ListView
CreateView

FormView
DetailView
UpdateView
DeleteView

"""


class HomeTemplateView(TemplateView):
    template_name = 'booksaw/index.html'


class AllBooksListView(ListView):
    template_name = 'booksaw/all_books.html'
    queryset = Book.objects.all()
    paginator_class = Paginator(object_list=queryset, per_page=100)

    extra_context = {
        'categories': Category.objects.all(),
    }


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'booksaw/book_create.html'
    success_url = reverse_lazy('apps:all_books')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.owner = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
