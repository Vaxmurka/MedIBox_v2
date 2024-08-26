from django.shortcuts import render
from django.http import JsonResponse
from patients.models import Patient, Pills, Taking
from users.models import User
import json


def send_json(request):
    users = User.objects.all()
    data = []

    for user in users:
        patients = Patient.objects.filter(user=user)

        for patient in patients:
            group = patient.groups
            water = patient.portion_of_water
            id = patient.fingerprint
            name = patient.first_name + ' ' + patient.username

            data_schedule = []
            takings = Taking.objects.filter(patient=patient)
            for taking in takings:
                quantity_pills = taking.quantity_pills
                time = taking.time

                data_pill = {}
                pills = Pills.objects.filter(taking=taking)
                for pill in pills:
                    name_p = pill.name
                    container = pill.container
                    data_pill = {
                        "Название": name_p,
                        "Контейнер": container,
                    }

                data_taking = {
                    "таблетка": data_pill,
                    "количество": quantity_pills,
                    # "время": time,
                    "дни": {
                        "понедельник": taking.monday,
                        "вторник": taking.tuesday,
                        "среда": taking.wednesday,
                        "четверг": taking.thursday,
                        "пятница": taking.friday,
                        "суббота": taking.saturday,
                        "воскресенье": taking.sunday,
                    },
                }
                data_schedule.append(data_taking)

            data_patient = {
                "Пользователь": name,
                "id": id,
                # "Группа": group,
                "Количество воды": water,
                "Расписание": data_schedule,
                "Опекун": user.username
            }
            data.append(data_patient)
    # print(data)
    json_data = json.dumps(data, ensure_ascii=False)
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(json_data)
    print(json_data)
    return JsonResponse(json_data, safe=False)
    # return json_data


def index(request):
    context = {
        'title': 'MedIBox - Устройства',
        'device': 'device',
        # 'data': send_json()
    }
    return render(request, "device.html", context)