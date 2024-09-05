from django.urls import path
from . import views
urlpatterns = [
    path("",views.mainadmin,name='mainadmin'),
    path("createform",views.createform,name='createform'),
    path("createclient",views.createclient,name='createclient'),
    path("createtrainer",views.createtrainer,name='createtrainer'),




]