import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from . import redis_utils


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Увеличиваем значения счетчика участников чата
        redis_utils.inc_room_count(self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Уменьшаем значение счетчика участников чата
        redis_utils.dec_room_count(self.room_name)

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Добавляем сообщение в redis, чтобы список сообщений чата был потом доступен для вновь прибывших участников
        redis_utils.add_message(self.scope['user'], self.room_name, message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']

        self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
