import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("The Scope------------>", self.scope)
        print("connect Event ------------>", event)
        print("The channel_name------------> ", self.channel_name)
        other_user = self.scope['url_route']['kwargs']['username']
        # other_user is the user who we want to communicate with
        # we send the message to their
        me = self.scope['user']
        """ Chat-Room """
        thread_obj = await self.get_thread(me, other_user)
        self.thread_obj = thread_obj
        print(
            "------------> " +
            f"Username who is sending: {me} and thread_obj_id: {thread_obj.id}")
        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        """
            When a message is received from the websocket
            {'type':'websocket.receive','text':'{"message":"abc"}'}
        """
        print("receive Event ------------>", event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            print(msg)
            user = self.scope['user']
            username = 'default'
            if user.is_authenticated:
                username = user.username
            myResponse = {
                'message': msg,
                'username': username
            }
            await self.create_chat_message(user, msg)

            ''' The below code --> Broadcast the "message-event" to be sent'''
            await self.channel_layer.group_send(
                self.chat_room,
                {
                    "type": "chat_message",
                    # this will actually call a custom function called `chat_message`
                    "text": json.dumps(myResponse)
                }
            )
    ''' The below code --> send the actual message'''
    async def chat_message(self, event):
        """ Custom function """
        print('message This should a `chat-message` type of event ------------>', event)
        await self.send({
            "type": "websocket.send",  # This will send the data to client
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)

    @database_sync_to_async
    def get_thread(self, user, other_username):
        return Thread.objects.get_or_new(user, other_username)[0]

    @database_sync_to_async
    def create_chat_message(self, me, msg):
        thread_obj = self.thread_obj
        # me = self.scope['user']
        return ChatMessage.objects.create(thread=thread_obj, user=me, message=msg)
