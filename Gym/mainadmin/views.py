from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse

def mainadmin(request):
    return render(request,"mainadmin/index.html")

def createform(request):
    return render(request,"mainadmin/createform.html")

def createclient(request):
    return render(request,"mainadmin/createclient.html")

def createtrainer(request):
    return render(request,"mainadmin/createtrainer.html")
