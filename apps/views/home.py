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


class HomeTemplateView(ListView):
    template_name = 'booksaw/index.html'
    model = Book

