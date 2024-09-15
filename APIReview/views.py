from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Human
from .serializers import HumanSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def getPeople(request):
    if request.method == 'GET':
        people = Human.objects.all()
        serializer = HumanSerializer(people, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getHuman(request, id):
    if request.method == 'GET':
        human = Human.objects.get(pk=id)
        serializer = HumanSerializer(human)
        return Response(serializer.data)