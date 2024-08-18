from typing import Any
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from users.models import User

from django.contrib.auth import logout
from django.shortcuts import redirect


def logreg(request):
    if request.method == "POST":
        forml = UserLoginForm(data=request.POST)
        formr = UserRegistrationForm(data=request.POST)
        if formr.is_valid():
            formr.save()
            user: Any = formr.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:logreg'))

        elif forml.is_valid():
            username: Any = request.POST['username']
            password: Any = request.POST['password']
            user: Any = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))

    else:
        forml = UserLoginForm()
        formr = UserRegistrationForm()

    context = {
        'forml': forml,
        'formr': formr
    }

    return render(request, 'users/logSig.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    x = User.objects.filter(id=request.user.id).values_list()[0][2]
    print(x)
    admin = ''
    if x: admin = 'True'

    context = {
        'title': 'MedIBox - Профиль',
        'content': 'Это ты',
        'form': form,
        'admin': admin
    }

    return render(request, "users/profile.html", context)


@login_required
def profile_delete(request):
    request.user.delete()

    return HttpResponseRedirect(reverse('users:logreg'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:logreg'))