from django.shortcuts import render
from django.http import JsonResponse
from patients.models import Patient
from users.models import User


def send_json(request):
    # Создайте JSON данные для отправки
    # users = User.objects.all()
    # for user in users:
    #     patients = Patient.objects.filter(user=user)
    #     for patient in patients:
    #         group = patient.groups
    #         water = patient.portion_of_water
    #         id = patient.fingerprint
    #         name = patient.first_name + patient.username
    #         schedule = patient.schedule

    data1 = {
        "message": "Hello from Django",
        "value": 42,
    }
    data = {
        "data": data1,
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