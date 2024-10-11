from django.shortcuts import render
from django.http import JsonResponse
from patients.models import Patient, Pills, Taking
from users.models import User
import json
from patients.serializer import PatientSerializer, TakingSerializer


def commit(username):
    # f = open('patient.json', 'w')
    # f.close()
    data = []
    dataTaking = []

    patients = Patient.objects.filter(user=username)
    for patient in patients:
        serializer = PatientSerializer(patient)
        dataPatient = serializer.data

        takings = Taking.objects.filter(patient=patient)
        for taking in takings:
            serial = TakingSerializer(taking)
            dataTaking = serial.data
            dataTaking['patient'] = dataPatient
            print(dataTaking)

            data.append(dataTaking)
            print(dataPatient)

            with open('patient.json', 'w') as outfile:
                json.dump(dataTaking, outfile)
    # print(dataTaking)
    return data


def send_json(request):
    data = []
    try:
        username = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        username = None

    users = User.objects.all()
    for user in users:
        patients = Patient.objects.filter(user=user)
        for patient in patients:
            serializer = PatientSerializer(patient)
            dataPatient = serializer.data

            takings = Taking.objects.filter(patient=patient)

            dataTaking = []
            for taking in takings:
                serial = TakingSerializer(taking)
                _dataTaking = serial.data
                # dataTaking['patient'] = dataPatient
                # print(dataTaking)

                # data.append(dataTaking)
                dataTaking.append(_dataTaking)

            dataPatient['taking'] = dataTaking
            dataPatient['user'] = user.username
            data.append(dataPatient)
    return JsonResponse(data, safe=False)


def index(request):
    try:
        username = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        username = None

    context = {
        'title': 'MedIBox - Устройства',
        'device': 'device',
        # 'data': commit(username)
    }
    return render(request, "device.html", context)