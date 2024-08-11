from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

import users.models
# from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'profile__card-input',
                                      'placeholder': 'Фамилия'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'profile__card-input',
                                          'placeholder': 'Пароль'})
    )

    class Meta:
        model = users.models.User
        fields: list[str] = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = users.models.User
        fields = (
            "role",
            "first_name",
            "username",
            "email",
            "telegram",
            "password1",
            "password2",

        )

    role = forms.ChoiceField(
        label='Роль',
        choices=(('1', "Пользователь"),
                 ('2', 'Мед. работник'),
                 ),
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
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'user@example.com',
            }
        )
    )
    telegram = forms.CharField(
        label='Имя',
        widget=forms.URLInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'https://t.me/user',
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Пароль',
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.TextInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'Подтверждение пароля',
            }
        )
    )


class ProfileForm(UserChangeForm):
    class Meta:
        model = users.models.User
        fields = (
            'role',
            'first_name',
            'username',
            "email",
            "telegram",
        )

    image = forms.ImageField(required=False)
    role = forms.ChoiceField(
        label='Роль',
        choices=(('1', "Пользователь"),
                 ('2', 'Мед. работник'),
                 ),
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
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'user@example.com',
            }
        )
    )
    telegram = forms.CharField(
        label='Телеграм',
        widget=forms.URLInput(
            attrs={
                'class': 'profile__card-input',
                'placeholder': 'https://t.me/user',
            }
        )
    )
