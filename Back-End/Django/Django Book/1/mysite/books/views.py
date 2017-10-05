from django.shortcuts import render

# Create your views here.
def search_form(request):
    return render(request, 'books/search_form.html')


from django.http import HttpResponse

from books.models import Book

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         books = Book.objects.filter(title__icontains=q)
#         return render(request, 'books/search_results.html',
#                       {'books': books, 'query': q})
#     else:
#         return HttpResponse('Please submit a search term.')

def search(request):
    # error = False
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            # error = True
            errors.append('Enter a search term.')
        elif len(q) > 20:
            # error = True
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books': books, 'query': q})
    return render(request, 'books/search_form.html', {'errors': errors})