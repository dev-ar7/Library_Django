from django.shortcuts import render
from .forms import StudentsForm, BookForm, IssueBookForm
from .models import Students, Book, IssueBook
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_form(request):
    form = StudentsForm
    context = {
        'form': form
    }
    return render(request, 'student_form.html', context)


def book_form(request):
    form = BookForm
    context = {
        'form': form
    }
    return render(request, 'book_form.html', context)


def issue_form(request):
    form = IssueBookForm
    context = {
        'form': form
    }
    return render(request, 'issue_form.html', context)


def new_student(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        form.save()
    return redirect('/show_students')


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
    return redirect('/show_books')


def new_issuebook(request):
    if request.method == "POST":
        form = IssueBookForm(request.POST)
        form.save()
    return redirect('/show_issuebooks')


def std_view(request):
    std = Students.objects.order_by('-id')
    context = {
        'std': std
    }
    return render(request, 'std_view.html', context)


def book_view(request):
    book = Book.objects.order_by('-id')
    context = {
        'book': book
    }
    return render(request, 'book_view.html', context)


def issuebook_view(request):
    issuebook = IssueBook.objects.order_by('-id')
    context = {
        'issuebook': issuebook
    }
    return render(request, 'issuebook_view.html', context)
