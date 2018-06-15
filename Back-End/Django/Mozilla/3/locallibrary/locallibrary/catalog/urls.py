from django.urls import path
from . import views

from message_board.views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    path('about/', AboutPageView.as_view(), name='notice_about'),
    path('contact/', ContactPageView.as_view(), name='notice_contact'),




# re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
#     path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
# path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]


# from django.urls import path
# from . import views

# urlpatterns = [

# ]