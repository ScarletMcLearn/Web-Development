from django.shortcuts import render

# Create your views here.
from .models import *
from django.views import generic

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )


class BookListView(generic.ListView):
    model=Book
    paginate_by = 1

    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'catalog/book_list.html'


    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

   
class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        #book_id=get_object_or_404(Book, pk=pk)
        
        return render(
            request,
            'catalog/book_detail.html',
            context={'book':book_id,}
        )