from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    # path('<slug:slug>', views.patient, name='patient_detail'),  # new
    path('patients/', views.allpatients, name='allpatients_list'),
    path('patients/<slug:patient_slug>/', views.patient_detail, name='patient'),
    path('newPatient', views.patient_reg, name='newPatient'),
]