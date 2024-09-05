from django.db import models

class user_login(models.Model):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=120)

class user_signup(models.Model):
    user_name = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=20)