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


def custom_filters(request):
    return render(request, template_name='books/custom_filters.html', context={
        'test_chars': 'UAOIUZKVNZLDJVO',
    })


def custom_tags(request):
    return render(request, template_name='books/custom_tags.html', context=None)


def advanced_custom_tags(request):
    return render(request, template_name='books/advanced_custom_tags.html', context=None)


def c2_related_objects(request):
    first_book = Book.objects.first()
    return render(request, template_name='books/c2_related_objects.html', context={
        'first_book': first_book,
    })


def c2_model_manager(request):
    title_count = None
    search_form_error = None
    query_placeholder = "Search"
    albert_books = Book.albert_objects.all()
    if request.method == 'POST':
        keyword = request.POST['keyword']
        if not keyword:
            search_form_error = "Empty search query."
        elif len(keyword) > 20:
            search_form_error = "Too long query."
        else:
            query_placeholder = keyword
            title_count = Book.objects.title_count(keyword)
    return render(request, 'books/c2_model_manager.html', {
        'title_count': title_count,
        'search_form_error': search_form_error,
        'query_placeholder': query_placeholder,
        'albert_books': albert_books,
    })
