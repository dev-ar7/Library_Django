from typing import ClassVar
from django import forms
from django.db import models
from django.forms import fields
from .models import Students, Book, IssueBook, returned_date

# Create Forms Here


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields = ['student', 'book', 'issue_date', 'return_date', 'score']
