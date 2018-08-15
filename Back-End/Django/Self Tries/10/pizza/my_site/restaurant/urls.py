from django.urls import path

from .views import AboutPageView, ContactUsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactUsPageView.as_view(), name='contact'),
    
]