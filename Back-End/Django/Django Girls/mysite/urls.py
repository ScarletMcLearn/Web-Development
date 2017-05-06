# Include these import statements...
from django.contrib import admin
# admin.autodiscover()

# And include this URLpattern...

from django.conf.urls import url

from django.conf.urls import include


urlpatterns = patterns('',
    # ...
    # (r'^admin/', include(admin.site.urls)),

    url(r'^admin/', admin.site.urls),  #added

    # ...

    # admin.autodiscover(),
)

# admin.autodiscover()
