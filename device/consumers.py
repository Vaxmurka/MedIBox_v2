from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        #
        # await self.send(text_data=json.dumps({
        #     'type': 'connection_established',
        #     'message': 'you are now connected'
        # }))

    def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Парсим входящие данные
        print(text_data)
        data = json.loads(text_data)
        question = data.get('question')
        user_id = data.get('user_id')
        print(data)

        # Вызов асинхронной функции для получения данных пользователя
        user_data = await self.get_user_data(user_id)

        # Отправляем ответ обратно клиенту
        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'user_data': user_data
        }))

    @database_sync_to_async
    def get_user_data(self, user_id):
        try:
            # Получаем информацию о пользователе
            user = User.objects.get(username=user_id)
            print(user)
            user_info = {
                'username': user.username,
                'email': user.email,
                'id': user.id,
                'data': {
                    'time': '12.00',
                    'type': 12,
                    'count': 1
                }
            }
            return {
                'user_info': user_info,
            }
        except User.DoesNotExist:
            return  {'error': 'User not found'}


        # # Пробуем распарсить текст как JSON
        # try:
        #     data = json.loads(text_data)
        #     message = data.get('message', '')  # Получаем сообщение
        #     print(message)
        #
        #     # Ответ на клиента
        #     await self.send(text_data=json.dumps({
        #         'response': f'You sent: {message}'
        #     }))
        # except json.JSONDecodeError:
        #     # Если произошла ошибка с JSON
        #     await self.send(text_data=json.dumps({
        #         'error': 'Invalid JSON!'
        #     }))