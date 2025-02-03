from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/signal/<str:session_id>/', consumers.SignalConsumer.as_asgi()),
    path('ws/chat/<str:session_id>/', consumers.ChatConsumer.as_asgi()),
]