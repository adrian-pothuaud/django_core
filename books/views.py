import sys

from django.shortcuts import render

# Create your views here.
from books.models import Book

sys.stdout = sys.stderr


def search_by_title(request):
    results = None
    if 'q' in request.GET and request.GET['q']:
        # form with request method have been submitted
        results = Book.objects.filter(title__icontains=request.GET['q'])
    if 'q' in request.POST and request.POST['q']:
        # form with post method have been submitted
        results = Book.objects.filter(title__icontains=request.POST['q'])
    return render(request, 'books/search_by_title.html', context={'results': results})


def search_by_valid_title(request):
    results = None
    get_method_errors = []
    post_method_errors = []

    print(request.GET)
    print(request.POST)

    if request.method == 'GET':
        # form with request method have been submitted

        try:
            q = request.GET['q']

            if not q:
                get_method_errors.append({
                    'abstract': 'Empty Query',
                    'message': 'You\'ve entered an empty search query ... Search query should not be empty!',
                    'instructions': 'Please enter a query not empty for your next try.'
                })

            elif len(q) > 20:
                get_method_errors.append({
                    'abstract': 'Too Long Query',
                    'message': 'You\'ve entered {}, this query is {} chars long ... '
                               'Search query should not be longer than 20 chars!'.format(q, len(q)),
                    'instructions': 'Please enter a shorter query.'
                })

            else:
                results = Book.objects.filter(title__icontains=request.GET['q'])

        except KeyError:
            pass

    if request.method == 'POST':
        # form with post method have been submitted

        try:
            q = request.POST['q']

            if not q:
                post_method_errors.append({
                    'abstract': 'Empty Query',
                    'message': 'You\'ve entered an empty search query ... Search query should not be empty!',
                    'instructions': 'Please enter a query not empty for your next try.'
                })

            elif len(q) > 20:
                post_method_errors.append({
                    'abstract': 'Too Long Query',
                    'message': 'You\'ve entered {}, this query is {} chars long ... '
                               'Search query should not be longer than 20 chars!'.format(q, len(q)),
                    'instructions': 'Please enter a shorter query.'
                })

            else:
                results = Book.objects.filter(title__icontains=request.POST['q'])

        except KeyError:
            pass

    context_dic = {
        'results': results,
        'get_method_errors': get_method_errors,
        'post_method_errors': post_method_errors
    }
    print(context_dic)

    return render(request, 'books/search_by_title_with_validation.html', context=context_dic)
