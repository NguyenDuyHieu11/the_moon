# from . import models
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from backend.the_moon.utils.redis_utils.redis_client import RedisManager

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        redis_manager = RedisManager()

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await redis_manager.initialize(self.room_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        

        # Send message to room group using the default channel_redis, this is to sending message between consumers and will not work 
        # if the connection is no longer active
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # This method of all consumers in the same group chat is triggered by the receive method
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
