
from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse

def landingpage(request):
    return render(request,"landingpage/landingpage.html")

class login_check(APIView):
    def post(self,request):
        email=request.POST["email"]
        password=request.POST["password"]
        if email == 'tarun@gmail.com':
            return JsonResponse({"status":"pass"})
        else:
            return JsonResponse({"status":"fail"})


