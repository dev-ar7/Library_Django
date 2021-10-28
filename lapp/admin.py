from django.contrib import admin
from .models import Students, Book, IssueBook

# Register your models here.

admin.site.register(Students)
admin.site.register(Book)
admin.site.register(IssueBook)
