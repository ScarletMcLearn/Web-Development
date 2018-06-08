from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='index'),
    path('translate/', views.translate, name='translate'),
    # path('books/', views.BookListView.as_view(), name='books'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # path('authors/', views.AuthorListView.as_view(), name='authors'),
    # path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    # path('about/', AboutPageView.as_view(), name='notice_about'),
    # path('contact/', ContactPageView.as_view(), name='notice_contact'),

]