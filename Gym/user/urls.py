from django.urls import path
from . import views
urlpatterns = [
    path("signup/",views.signup,name='signup'),
    path("login/",views.login,name='login'),
    path("create_user", views.create_user.as_view(),name="create_user"),
    path("view_user", views.view_user.as_view(),name="view_user"),
    path("login_user", views.login_user.as_view(),name="login_user"),
    path("view_login", views.view_login.as_view(),name="view_login"),
    path("removereference", views.removereference.as_view(),name="removereference"),
    path("removesignup", views.removesignup.as_view(),name="removesignup"),







    

]