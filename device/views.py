from django.shortcuts import render
from django.http import JsonResponse
from patients.models import Patient, Pills, Taking
from users.models import User
import json


# def send_json():
#     # Создайте JSON данные для отправки
#     users = User.objects.all()
#     data = []
#
#     for user in users:
#         patients = Patient.objects.filter(user=user)
#
#         for patient in patients:
#             group = patient.groups
#             water = patient.portion_of_water
#             id = patient.fingerprint
#             name = patient.first_name + ' ' + patient.username
#
#             schedules = Schedule.objects.filter(patient=patient)
#
#             data_patient = {
#                 'Пользователь': name,
#                 'id': id,
#                 'Группа': group,
#                 'Количество воды': water,
#                 'Расписание': schedules,
#                 'Опекун': user.username
#             }
#             data.append(data_patient)
#     print(data)
#     return data

def send_json():
    # Создайте JSON данные для отправки
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

                # pill = Pills.objects.filter(taking=taking)
                # pill = Pills.objects.filter(t)
                # name_p = pill.name
                # container = pill.container

                data_taking = {
                    # 'таблетка': {
                    #     'Название': name_p,
                    #     'Контейнер': container,
                    # },
                    'количество': quantity_pills,
                    'время': time,
                    'дни': {
                        'понедельник': taking.monday,
                        'вторник': taking.tuesday,
                        'среда': taking.wednesday,
                        'четверг': taking.thursday,
                        'пятница': taking.friday,
                        'суббота': taking.saturday,
                        'воскресенье': taking.sunday,
                    },
                }
                data_schedule.append(data_taking)
                print(data_taking)

            data_patient = {
                'Пользователь': name,
                'id': id,
                'Группа': group,
                'Количество воды': water,
                'Расписание': data_schedule,
                'Опекун': user.username
            }
            data.append(data_patient)
    print(data)
    return data



def index(request):
    context = {
        'title': 'MedIBox - Устройства',
        'device': 'device',
        'data': send_json()
    }
    return render(request, "device.html", context)