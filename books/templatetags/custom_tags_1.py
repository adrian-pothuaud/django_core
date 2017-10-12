import datetime

from django import template
from django.contrib.auth.models import User

from books.models import Book


register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag('books/books.html')
def show_books():
    return {
        'books': Book.objects.all()
    }


@register.assignment_tag
def show_users():
    return {
        'users': User.objects.all()
    }
