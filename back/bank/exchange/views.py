from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
import requests
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


def exchange_rate_view(request):
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
    params = {
        'authkey': 'iC53p9pJurfJjs1QHmJRxBTrjoL6Lgu5',
        'data': 'AP01'
    }   
    response = requests.get(url, params=params)
    return response    
  
@api_view(['GET'])
def get_exchange(request):
    data = exchange_rate_view(request).json()
    return Response(data)