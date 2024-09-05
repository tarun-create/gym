from django.urls import path
from . import views
urlpatterns = [
    path("landingpage/",views.landingpage,name='landingpage'),
    path("login_check",views.login_check.as_view(),name="login_check")
    

]