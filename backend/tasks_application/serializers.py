from rest_framework import serializers
from .models import Task_Model

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Task_Model
        fields="__all__"