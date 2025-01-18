from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from patients.forms import PatientsForm
from patients.models import Patient, Groups, Taking
from users.models import User
import datetime


def index(request):
    user = request.user
    data_group = None
    patients = Patient.objects.filter(user=user)

    context = {
        'title': 'MedIBox - Главная',
        'group': data_group,
        'patients': patients,
        'next_taking': 0,
        'user': user,
        'main': 'main',
    }
    return render(request, 'main/index.html', context)
