from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView       # Generic List (Class Based) View
from .models import Post        # Model For List View

# To Turn Off Caching ####################################
from django.views.decorators.cache import never_cache    #   
from django.utils.decorators import method_decorator     #
##########################################################

@method_decorator(never_cache, name='dispatch')     # To Turn Off Caching
class HomePageView(ListView):    # Making Class Based (List) View 
    model = Post                 # Model for List View
    template_name = 'index.html' # Template for Class Based View 

    context_object_name = 'posts'  # Default: object_list   # Template Context to use as Template Tags

    # For Pagination ################################################
    paginate_by = 1     # Number of items (per page) to Paginate by #                                                                  #
    queryset = Post.objects.all()  # Default: Model.objects.all()   #
    # ^List of all objects to paginate                              #
    #################################################################