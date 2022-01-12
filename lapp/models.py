from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class Students(models.Model):
    std_id = models.CharField(max_length=25)
    std_name = models.CharField(max_length=250)
    std_address = models.CharField(max_length=500)
    std_batch = models.CharField(max_length=100)

    def __str__(self):
        return (self.std_name + " " + self.std_id)


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=150)
    book_pages = models.IntegerField()

    def __str__(self):
        return self.book_title


# Creating A return_date Function To Use Later In The Class
def returned_date():
    return datetime.today() + timedelta(days=7)


class IssueBook(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default="DD-MM-YYYY")
    return_date = models.DateTimeField(default=returned_date)
    score = models.CharField(max_length=3, default="Some Scores")

    def __str__(self):
        return self.student.std_name + "Borrowed" + self.book.book_title
