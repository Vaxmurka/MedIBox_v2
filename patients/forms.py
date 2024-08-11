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
