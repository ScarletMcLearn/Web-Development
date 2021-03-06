from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView

from django.views.decorators.cache import never_cache

# @never_cache

from django.utils.decorators import method_decorator

@method_decorator(never_cache, name='dispatch')
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
