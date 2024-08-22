from django.urls import path
from . import views

app_name = 'device'

urlpatterns = [
    # path('<slug:slug>', views.patient, name='patient_detail'),  # new
    path('device/', views.index, name='device'),
    # path('send_json/', views.send_json, name='send_json'),
]