from django.shortcuts import render

# Create your views here.
from django.views import generic

class HomePageView(generic.TemplateView):

    template_name = "notice_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context



class AboutPageView(generic.TemplateView):

    template_name = "notice_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context