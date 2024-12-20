from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView

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
