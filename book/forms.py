from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=[
            'title',
            'isbn',
            'page',
            'category',
            'author_id',
            'description',
            'price',
            'quantity',
            'image'


        ]