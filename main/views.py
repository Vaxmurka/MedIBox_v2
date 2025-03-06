from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from patients.forms import PatientsForm
from patients.models import Patient, Groups, Taking, Pills
from users.models import User
import datetime


def index(request):
    user = request.user
    data_group = None
    patients = Patient.objects.filter(user=user)
    pillsData = Pills.objects.all()

    names = [pill.name for pill in pillsData]
    containers = [pill.container for pill in pillsData]
    pills = {k: v for k, v in zip(containers, names)}
    print(pills)


    context = {
        'title': 'MedIBox - Главная',
        'group': data_group,
        'patients': patients,
        'countPatients': len(patients),
        'phone': '+7 (900) 123 45-67',
        'pills': pills,
        'user': user,
        'main': 'main',
    }
    return render(request, 'main/index.html', context)
