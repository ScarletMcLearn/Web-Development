from django.urls import path

from . import views 

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),    # Url Pattern to Class based view as view
]