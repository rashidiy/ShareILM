from django import forms

from apps.models import Book


class CommentForm(forms.Form):
    text = forms.CharField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'price',
            'category',
            'format',
            'availability',
            'book_image',
            'description',
            'publisher',
            'isbn',
            'quantity',
        ]
