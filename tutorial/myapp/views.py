from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.serializers import PersonSerializer
from myapp.models import Person

from django.http import HttpResponse
import requests

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

@api_view(['GET', 'POST'])
def info(request):
    endpoint = 'https://api.github.com'
    requestUrl = endpoint + '/search/users'
    params = {'q': 'winsung'} 
    response = requests.get(requestUrl, params=params)
    
    return Response(response.json())
