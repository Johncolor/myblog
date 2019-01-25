# -*- coding: utf8 -*-
from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index),
    url(r'^create/', create),
    url(r'^update/', update),
    url(r'^delete/', delete),

    url(r'^get_data/', get_data),
    # url(r'^admin/', admin.site.urls),
]

urls = urlpatterns