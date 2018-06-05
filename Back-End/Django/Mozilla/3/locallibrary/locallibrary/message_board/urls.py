from django.urls import path

from message_board.views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='notice_home'),
    path('about', AboutPageView.as_view(), name='notice_about'),
]