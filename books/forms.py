from django import forms
from .models import Books


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'author',
            'publisher',
            'year_published',
            'description',
            'url',
            'image_url',
        ]