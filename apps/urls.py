from django.urls import path
from apps.views import HomeTemplateView, AllBooksListView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('all_books/', AllBooksListView.as_view(), name='all_books'),
]
