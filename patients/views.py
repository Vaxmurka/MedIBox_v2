from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
# from patients.forms import PatientsForm
from patients.models import Patient, Groups, Taking
from patients.forms import PatientsForm, TakingForm, PillsForm, VoiceForm, GroupsForm
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
        'group': data_group,
        # 'groups': groups,
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
        'phone_number': patient[7],
    }
    return render(request, 'patient.html', context)


def create_patient(request):
    if request.method == 'POST':
        print(request.POST)
        formp = PatientsForm(data=request.POST)
        formv = VoiceForm(data=request.POST, files=request.FILES)
        formg = GroupsForm(data=request.POST)

        if formp.is_valid():
            patient = formp.save(commit=False)  # Не сохраняем еще в БД
            patient.user = request.user  # Присваиваем текущего пользователя
            patient.save()  # Теперь сохраняем в БД
            print('formp.good')
            return HttpResponseRedirect(reverse('patients:allpatients_list'))
        else:
            print('form.errors', formp.errors)

        if formv.is_valid():
            formv.save()
            print('formv.good')
            return HttpResponseRedirect(reverse('patients:newpatient'))
        else:
            print('form.errors', formv.errors)

        if formg.is_valid():
            formg.save()
            print('formg.good')
            return HttpResponseRedirect(reverse('patients:newpatient'))
        else:
            print('form.errors', formv.errors)
    else:
        print('form.null')
        formp = PatientsForm()
        formv = VoiceForm()
        formg = GroupsForm()

    context = {
        "formp": formp,
        'formv': formv,
        'formg': formg,
    }

    return render(request, 'createPatient.html', context)


def create_taking(request):
    if request.method == 'POST':
        formt = TakingForm(data=request.POST)
        formpi = PillsForm(data=request.POST)

        if formt.is_valid():
            formt.save()
            return HttpResponseRedirect(reverse('patients:allpatients_list'))
        else:
            print('form.errors', formt.errors)

        if formpi.is_valid():
            formpi.save()
            return HttpResponseRedirect(reverse('patients:newtaking'))
        else:
            print('formpi.errors', formpi.errors)
    else:
        print('form.null')
        formt = TakingForm()
        formpi = PillsForm()

    context = {
        "formt": formt,
        'formpi': formpi,
    }

    return render(request, 'createTaking.html', context)
