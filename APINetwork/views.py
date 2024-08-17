from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Information
from .serializers import InformationSerializer


@api_view(['GET', 'POST'])
def host(request):
    if request.method == 'GET':
        id = request.GET.get('id', '1')
        query = Information.objects.get(id=id)
        serializer = InformationSerializer(query)
        return Response(serializer.data)
    elif request.method == 'POST':
        query = InformationSerializer(data=request.data)
        if query.is_valid():
            query.save()
            return Response(query.data, status=status.HTTP_201_CREATED)
        return Response(query.errors, status=status.HTTP_400_BAD_REQUEST)
