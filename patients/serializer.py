# serializer.py
from rest_framework import serializers
from .models import Patient, Groups, Taking, Pills, Voices


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'username', 'first_name', 'number', 'portion_of_water']


class TakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taking
        fields = ['patient', 'pills', 'time', 'quantity_pills', 'monday', 'tuesday', 'wednesday',
                  'thursday', 'friday', 'saturday', 'sunday']