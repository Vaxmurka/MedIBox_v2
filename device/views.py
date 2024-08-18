from django.shortcuts import render
from django.http import JsonResponse


def send_json(request):
    # Создайте JSON данные для отправки
    data = {
        "message": "Hello from Django",
        "value": 42,
        "type": "test message",
        "length": 5,
        "name": "Hello ESP32"
    }
    return JsonResponse(data)


def index(request):
    context = {
        'title': 'MedIBox - Устройства',
        'device': 'device',
    }
    return render(request, "device.html", context)