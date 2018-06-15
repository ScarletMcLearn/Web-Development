from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.views.generic import ListView
from .models import Notice

class HomePageView(generic.ListView):
    model = Notice
    template_name = "message_board/blog.html"

    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        context['notice_list'] = Notice.objects.all()
        return context



class AboutPageView(generic.TemplateView):

    template_name = "message_board/notice_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context




class ContactPageView(generic.TemplateView):

    template_name = "message_board/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context