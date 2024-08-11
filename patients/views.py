from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
# from patients.forms import PatientsForm
from patients.models import Patient, Groups
from django.contrib.auth.decorators import login_required
from users.models import User


def allpatients(request, group_slug=None):
    group = None
    groups = Groups.objects.all()
    patients = Patient.objects.all()
    role: int = User.get_role(request.user) #request.user

    if group_slug:
        group = get_object_or_404(Groups, slug=group_slug)
        patients = Patient.objects.all()

    context = {
        'title': 'MedIBox - Пользователи',
        'group': group,
        'groups': groups,
        'patients': patients,
        'role': role,
    }
    return render(request, 'allPatients.html', context)


# def patient_detail(request, id, slug=1):
#     patient = get_object_or_404(Patient, id=id, slug=slug, available=True)
#
#     context = {'patient': patient}
#     return render(request, 'patient.html', context)

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


