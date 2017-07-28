"""boardgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name = 'boardgames_home'),
]

urlpatterns += patterns('django.contrib.auth.views', url(r'^login/$', 'login', {'template_name' : 'login_html'}, name = 'boardgames_login'),
url(r'^logout/$', 'logout', {'next_page' : 'boardgames_home'}, name='boardgames_logout'),)
