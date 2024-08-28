from django import forms
from django.forms import ModelForm

from patients.models import Patient, Groups, Voices
from users.models import User


class PatientsForm(ModelForm):
    class Meta:
        model = Patient
        fields = (
            'user',
            'group',
            'voices',
            'first_name',
            'username',
            'fingerprint',
            'number',
            'portion_of_water',
            # 'slug',
        )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Пользователь',
        widget=forms.Select(
            attrs={'class': 'profile__card-select'}
        ),
    )
    group = forms.ModelChoiceField(
        queryset=Groups.objects.all(),
        label='Группа',
        widget=forms.Select(
            attrs={'class': 'profile__card-select'}
        ),
    )
    voices = forms.ModelChoiceField(
        queryset=Voices.objects.all(),
        label='Озвучка',
        widget=forms.Select(
            attrs={'class': 'profile__card-select'}
        ),
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
        label='Id отпечатка',
        widget=forms.NumberInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': '0',
            }
        )
    )
    number = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': '+ 7 900 000 00-00',
            }
        )
    )
    portion_of_water = forms.IntegerField(
        label='Порция воды',
        widget=forms.NumberInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': '150',
            }
        )
    )
    # slug = forms.SlugField(
    #     label='ID',
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'profile__card-input',
    #             'placeholder': '0',
    #         }
    #     )
    # )
