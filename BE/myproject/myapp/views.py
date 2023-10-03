from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")