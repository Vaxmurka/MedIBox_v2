from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from patients.forms import PatientsForm
from patients.models import Patient, Groups
from users.models import User


# def index(request):
#
#     context = {
#         'title': 'MedIBox - Главная',
#         'main': 'main',
#
#     }
#
#     return render(request, "main/index.html", context)


def index(request):
    users = User.objects.all()
    data_group = None
    patients = Patient.objects.filter(user_id=request.user.id)
    for user in users:

        groups = Groups.objects.filter(user=user)
        for group in groups:
            group = group.name
            data_group = group

    context = {
        'title': 'MedIBox - Главная',
        'group': data_group,
        'patients': patients,
        # 'patient': 'patient',
        'main': 'main',
    }
    return render(request, 'main/index.html', context)