from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url, re_path
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chat.consumers import ChatConsumer
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('messages/<str:username>/', ChatConsumer),
                    # url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer),
                    # re_path(r'^ws/chat/(?P<room_name>[^/]+)/', ChatConsumer),
                ]
            )
        )
    )
})
