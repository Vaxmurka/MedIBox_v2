from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from users.models import User
import time
from datetime import datetime, time, timedelta

from patients.models import Patient, Taking


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
            list_patients = []
            print(user)
            patients = Patient.objects.filter(user=user)

            for patient in patients:
                print(patient.username)
                takings = Taking.objects.filter(patient=patient)
                print(takings)

                for taking in takings:

                    user_info = {
                        'username': patient.username,
                        'id': patient.fingerprint,
                        'data': {
                            'time': taking.time,
                            'type': taking.pills.container,
                            'count': taking.quantity_pills
                        }
                    }
                    user_weekday = [
                        taking.monday,
                        taking.tuesday,
                        taking.wednesday,
                        taking.thursday,
                        taking.friday,
                        taking.saturday,
                        taking.sunday
                    ]
                    print(user_weekday)
                    if check_patient_time(user_info['data']['time'], user_weekday):
                        list_patients.append(user_info)


            print(list_patients)
            if len(list_patients)>0:
                min_time_patient = min(list_patients, key=lambda x: x['data']['time'])
                min_time_patient_json = json.dumps(min_time_patient, default=str)

                return {'user_info': min_time_patient_json}
            else:
                return {'user_info': None}
        except User.DoesNotExist:
            return {'error': 'User not found'}


def check_patient_time(time1, uw) -> bool:
    time2=datetime.now().time()
    dt1 = datetime.combine(datetime(1900, 1, 1), time1)
    dt2 = datetime.combine(datetime(1900, 1, 1), time2)

    difference = dt1 - dt2
    difference = difference.total_seconds()

    today = datetime.today()
    wd = today.weekday()
    print()

    if difference >= 0 and (uw[wd]==True):
        return True
    else:
        return False


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