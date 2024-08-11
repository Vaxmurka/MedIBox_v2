from typing import Any
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request) -> Any | HttpResponse:
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username: Any = request.POST['username']
            password: Any = request.POST['password']
            user: Any = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    context: dict[str, Any] = {
        'title': 'MedIBox - Авторизация',
        'form': form
    }

    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user: Any = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'MedIBox - Регистрация',
        'form': form

    }

    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'MedIBox - Профиль',
        'content': 'Это ты',
        'form': form
    }

    return render(request, "users/profile.html", context)