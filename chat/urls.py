from django.conf.urls import url
from django.urls import path, re_path

from .views import index, room

app_name = 'chat'

urlpatterns = [
    path(r'', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
