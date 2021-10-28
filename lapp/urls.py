from django.conf.urls import url
from . import views


app_name = "lapp"


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_form', views.student_form, name='student_form'),
    url(r'^book_form', views.book_form, name='book_form'),
    url(r'^issue_form', views.issue_form, name='issue_form'),
    url(r'new_student', views.new_student, name='new_student'),
    url(r'^new_book', views.new_book, name='new_book'),
    url(r'^new_issuebook', views.new_issuebook, name='new_issuebook'),
    # std_view = Student_view
    url(r'^show_students', views.std_view, name='std_view'),
    url(r'^show_books', views.book_view, name='book_view'),
    url(r'^show_issuebooks', views.issuebook_view, name='issuebook_view'),
]
