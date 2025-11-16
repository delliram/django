from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task_Model
from .serializers import Task_Serializer
# Create your views here.


@api_view(['GET'])
def TaskView(request):
    if request=="GET":
        model=Task_Model.objects.all()
        serializer=Task_Serializer(model,many=True)
        return Response(serializer.data)