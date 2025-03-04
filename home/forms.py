from django import forms
from . import models


class bookForm(forms.ModelForm):
    class Meta:
        model = models.book
        fields = ['title', 'author', 'isbn', 'price', 'description', 'image']
        