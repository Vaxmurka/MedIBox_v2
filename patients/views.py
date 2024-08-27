from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from patients.forms import PatientsForm
from patients.models import Patient
from django.contrib.auth.decorators import login_required


def allpatients(request):
    patients = Patient.objects.filter(user_id=request.user.id)

    # if request.method == 'POST':
    #     form = PatientsForm(data=request.POST)
    #     print('form.created')
    #     if form.is_valid():
    #         print('form.save')
    #         form.save()
    #         return HttpResponseRedirect(reverse('patients:allpatients_list'))
    #     else:
    #         print('form.errors')
    # else:
    #     print('form.null')
    #     form = PatientsForm()

    context = {
        'title': 'MedIBox - Пользователи',
        'patients': patients,
        'patient': 'patient',
        # "form": form,
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


def create_patient(request):
    if request.method == 'GET':
        form = PatientsForm(data=request.POST)
        if form.is_valid():
            print('form.save')
            form.save()
            return HttpResponseRedirect(reverse('patients:allpatients_list'))
        else:
            print('form.errors')
    else:
        print('form.null')
        form = PatientsForm()

    return render(request, 'createPatient.html', {'form': form})