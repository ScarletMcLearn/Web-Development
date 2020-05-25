from django.contrib import admin
from django.urls import path, include

import cueeneh.urls
import user.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user.urls, namespace='user')),
    path('', include(cueeneh.urls, namespace='questions')),
]
