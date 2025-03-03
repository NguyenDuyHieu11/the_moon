# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()), #We call the as_asgi() classmethod in order to get an ASGI application that will instantiate an instance of our consumer for each user-connection. This is similar to Django’s as_view(), which plays the same role for per-request Django view instances.
]

# websocket_urlpatterns = [
#     path('ws/chat/', consumers.ChatConsumer.as_asgi()),
# ]zzfssf

