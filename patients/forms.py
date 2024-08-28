from django import forms
from django.contrib.auth.forms import UserCreationForm

from patients.models import Patient, Voices, Groups
from users.models import User


class PatientsForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = (
            "user",
            "groups",
            "first_name",
            "username",
            "fingerprint",
            "portion_of_water",
            "number",
            "voices",

        )

    user = forms.ChoiceField(
        label='Пользователь',
        choices=(User.objects.get(id=id)),
        widget=forms.Select(
            attrs={
                "class": 'profile__card-select'
            }
        )
    )
    groups = forms.ChoiceField(
        label='Пользователь',
        choices=(Groups.objects.get(id=id)),
        widget=forms.Select(
            attrs={
                "class": 'profile__card-select'
            }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Имя',
            }
        )
    )
    username = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Фамилия',
            }
        )
    )
    fingerprint = forms.IntegerField(
        label='Finger ID',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Finger ID',
            }
        )
    )
    portion_of_water = forms.CharField(
        label='Порция воды',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': '000',
            }
        )
    )
    number = forms.CharField(
        label='Телефон',
        widget=forms.NumberInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': '+7 (900) 000 00-00',
            }
        )
    )
    voices = forms.ChoiceField(
        label='Звуки',
        choices=(Voices.objects.get(id=id)),
        widget=forms.Select(
            attrs={
                "class": 'profile__card-select'
            }
        )
    )
    # voices = forms.CharField(
    #     label='Подтверждение пароля',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'profile__card-input',
    #             'placeholder': 'Подтверждение пароля',
    #         }
    #     )
    # )

