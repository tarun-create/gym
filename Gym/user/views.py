from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse
from user.models import user_signup
from user.models import user_login



def signup(request):
    return render(request,"user/signup.html")

def login(request):
    return render(request,"user/login.html")

class create_user(APIView):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        utype = request.POST['utype']
        usr = user_signup()
        usr.user_name = username
        usr.email = email
        usr.password = password
        usr.role = utype
        usr.save()
        return JsonResponse({"status": "pass"})
    
from django.views.generic import TemplateView

class view_user(TemplateView):
    template_name = "view_signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = user_signup.objects.all()
        context = { 'userdata': user_data}
        return context
    

class removereference(APIView):
     def post(self,request):
        name = request.POST['email']
        user_login.objects.filter(email=name).delete()
        return JsonResponse({"status":"pass"})
    

class login_user(APIView):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['pass']
        log = user_login()
        log.email = email
        log.password = password
        log.save()
        return JsonResponse({"status": "pass"})
    
class view_login(TemplateView):
    template_name = "view_login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = user_login.objects.all()
        context = { 'userdata': user_data}
        return context
    
class removesignup(APIView):
     def post(self,request):
        name = request.POST['user_name']
        user_signup.objects.filter(user_name=name).delete()
        return JsonResponse({"status":"pass"})
