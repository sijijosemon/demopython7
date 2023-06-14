from django.db import models

class login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
class registern(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    address =models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    materials_provide = models.CharField(max_length=250)



