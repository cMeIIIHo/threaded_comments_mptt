from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'(?P<post_id>[0-9]+)/$', post_detail, name='post_detail')
]
