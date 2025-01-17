import json
from websocket import create_connection


def SendQuestion(user):
    # Установить соединение с сервером
    ws = create_connection("ws://192.168.0.102:8000/ws")

    # Задайте user_id и вопрос
    user_id = user  # ID пользователя, к которому привязано устройство
    question = "Какой статус?"

    # Создайте JSON объект
    data_to_send = json.dumps({'user_id': user_id, 'question': question})

    # Отправьте данные
    ws.send(data_to_send)

    # Получите ответ
    response = json.loads(ws.recv())
    print(f'Response: {response}')

    # # Закройте соединение
    # ws.close()


if __name__ == '__main__':
    while True:
        msg = input('Enter a username: ')
        if msg == 'quit':
            break

        SendQuestion(msg)