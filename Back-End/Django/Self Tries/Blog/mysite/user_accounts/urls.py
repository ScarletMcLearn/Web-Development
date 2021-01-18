from django.urls import include, path

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.openLoginPage, name='login'),

    path('validate/', views.checkUser, name='checkUser'),
    # path("<slug>", views.detail, name='detail'), #, name = "unique_slug"
    # path("edit/<slug>", views.edit, name='edit'),

    path('accounts/', include('allauth.urls'), name='allauth-urls'),   # AllAuth
    # path('accounts/', include('user_accounts.urls')),
]