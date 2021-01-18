from django.urls import include, path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path("<slug>", views.detail, name='detail'), #, name = "unique_slug"
    path("edit/<slug>", views.edit, name='edit'),

    # path('accounts/', include('allauth.urls')),
    # path('account/', include('user_accounts.urls')),
]