from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# @never_cache
@method_decorator(never_cache, name='dispatch')
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'

    # @method_decorator(never_cache)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProtectedView, self).dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     posts = Post.objects.all()
    #     return posts

    def get_context_data(self, **kwargs):
        '''
        Eita Diye Template Context Set Korte Hoy
        '''
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['posts'] = Post.objects.all()

        return context
