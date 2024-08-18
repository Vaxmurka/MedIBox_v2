from django.shortcuts import render


def index(request):
    context = {
        'title': 'MedIBox - Устройства',
        'device': 'device',
    }
    return render(request, "device.html", context)