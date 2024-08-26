from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
# from patients.forms import PatientsForm
from patients.models import Patient, Groups
from django.contrib.auth.decorators import login_required
from users.models import User


def allpatients(request):
    users = User.objects.all()
    data_group = None
    patients = Patient.objects.filter(user_id=request.user.id)
    for user in users:

        groups = Groups.objects.filter(user=user)
        for group in groups:
            group = group.name
            data_group = group
            # data_group = {
            #     'what': group
            # }
    # print(group[0][1])
    # [0][1]

    context = {
        'title': 'MedIBox - Пользователи',
        'group': data_group,
        # 'groups': groups,
        'patients': patients,
        'patient': 'patient',
    }
    return render(request, 'allPatients.html', context)


def patient_detail(request, patient_slug):
    patient = list(Patient.objects.filter(slug=patient_slug).values_list()[0])
    p = Patient.objects.filter(slug=patient_slug).values()

    title = 'MedIBox - Пользователи/' + patient[4]

    context = {
        'title': title,
        'group': patient[2],
        'id': patient[5],
        'first_name': patient[3],
        'username': patient[4],
        'portion_of_water': patient[6],
        'phone_number': patient[7]
    }
    return render(request, 'patient.html', context)


