from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response({'message': 'api view'}, status=200)
    
    elif request.method == 'POST':
        return Response(request.data, status=200)