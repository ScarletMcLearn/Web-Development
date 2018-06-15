from django.urls import path

from message_board.views import HomePageView, AboutPageView, ContactPageView

# from django.conf import settings
# from django.conf.urls.static import static 

urlpatterns = [
    path('', HomePageView.as_view(), name='notice_home'),
    path('about/', AboutPageView.as_view(), name='notice_about'),
    path('contact/', ContactPageView.as_view(), name='notice_contact'),
]  
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)