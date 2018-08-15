from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class AboutPageView(TemplateView):

    template_name = "restaurant/about.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

class ContactUsPageView(TemplateView):

    template_name = "restaurant/contact.html"