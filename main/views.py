from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        'title': 'MedIBox - Главная',
        'content': 'Веб-интерфейс управления таблетницами MedIBox',
    }

    return render(request, "main/index.html", context)