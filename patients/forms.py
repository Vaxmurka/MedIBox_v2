# from django import forms
# from django.contrib.auth.forms import UserChangeForm
#
# from patients.models import Patient
#
#
# class PatientsForm(UserChangeForm):
#     class Meta:
#         model = Patient
#         fields = (
#             'first_name',
#             'username',
#             'fingerprint',
#             'portion_of_water',
#         )
#
#     first_name = forms.CharField(
#         label='Имя',
#         widget=forms.TextInput(
#             # attrs={
#             #     'class': 'form-control',
#             # }
#         )
#     )
#     username = forms.CharField(
#         label='Фамилия',
#         widget=forms.TextInput(
#             # attrs={
#             #     'class': 'form-control',
#             # }
#         )
#     )
#     fingerprint = forms.IntegerField(
#         label='Id отпечатка',
#         widget=forms.IntegerField(
#             # attrs={
#             #     'class': 'form-control',
#             # }
#         )
#     )
#     portion_of_water = forms.IntegerField(
#         label='Порция воды',
#         widget=forms.IntegerField(
#             # attrs={
#             #     'class': 'form-control',
#             # }
#         )
#     )
from django import forms
from django.forms import ModelForm

from patients.models import Patient, Groups, Voices, Taking, Pills
from users.models import User


class PatientsForm(ModelForm):
    class Meta:
        model = Patient
        fields = (
            # 'user',
            'groups',
            'voices',
            'first_name',
            'username',
            'fingerprint',
            'number',
            'portion_of_water',
            # 'slug',
        )

    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     label='Пользователь',
    #     widget=forms.Select(
    #         attrs={'class': 'profile__card-select'}
    #     ),
    # )
    # user = widget=forms.HiddenInput(
    #         attrs={'class': 'profile__card-select'}
    #     )
    groups = forms.ModelChoiceField(
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
    slug = {"slug": ("username",)}


class VoiceForm(ModelForm):
    class Meta:
        model = Voices
        fields = (
            'name',
            'voice',
        )
    name = forms.CharField(
        label='Названия звука',
        widget=forms.TextInput(
            attrs={'class': 'profile__card-input'}
        ),
    )
    voice = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'style': 'color:var(--app-content-main-color)'
            }
        )
    )


class GroupsForm(ModelForm):

    class Meta:
        model=Groups
        fields = (
            'user',
            'name',
        )

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Пользователь',
        widget=forms.Select(
            attrs={'class': 'profile__card-select'}
        ),
    )
    name = forms.CharField(
        label='Название группы',
        widget=forms.TextInput(
            attrs={'class': 'profile__card-input'}
        ),
    )
    slug = {"slug": ("name",)}
# ================================================================================================


class TakingForm(ModelForm):
    class Meta:
        model = Taking
        fields = (
            # 'user',
            'patient',
            'pills',
            'time',
            'quantity_pills',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        )

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        label='Пациент',
        widget=forms.Select(
            attrs={'class': 'profile__card-select'}
        ),
    )
    pills = forms.ModelChoiceField(
        queryset=Pills.objects.all(),
        label='таблетка',
        widget=forms.Select(
            attrs={'class': 'profile__card-select'}
        ),
    )
    time = forms.TimeField(
        label='Время',
        widget=forms.TimeInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Время',
            }
        )
    )
    quantity_pills = forms.IntegerField(
        label='Кол-во таблеток',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Кол-во таблеток',
            }
        )
    )
    monday = forms.TypedChoiceField(
        label='Понедельниу',
        widget=forms.CheckboxInput,
    )
    tuesday = forms.TypedChoiceField(
        label='Вторник',
        widget=forms.CheckboxInput,
    )
    wednesday = forms.TypedChoiceField(
        label='Среда',
        widget=forms.CheckboxInput,
    )
    thursday = forms.TypedChoiceField(
        label='Четверг',
        widget=forms.CheckboxInput,
    )
    friday = forms.TypedChoiceField(
        label='Пятница',
        widget=forms.CheckboxInput,
    )
    saturday = forms.TypedChoiceField(
        label='суббота',
        widget=forms.CheckboxInput,
    )
    # sunday = forms.ChoiceField(
    #     label='воскресенье',
    #     choices=(('1', "Да"),
    #              ('2', 'Нет'),
    #              ),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'taking__card-select',
    #         }
    #     )
    # )
    sunday = forms.TypedChoiceField(
        label='воскресенье',
        widget=forms.CheckboxInput,
    )


class PillsForm(ModelForm):
    class Meta:
        model = Pills
        fields = (
            # 'user',
            'name',
            'container',
        )

    name = forms.CharField(
        label='Название таблетки',
        widget=forms.TextInput(
            attrs={'class': 'profile__card-input',
                   'placeholder': 'Название таблеток:'
                   }
        ),
    )
    container = forms.IntegerField(
        label='контейнер',
        widget=forms.TextInput(
            attrs={'class': 'profile__card-input',
                   'placeholder': 'Номер контейнера:'
                   }
        ),
    )
