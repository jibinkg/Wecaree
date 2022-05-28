from django.db import models

# Create your models here.
class bookingform(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    Place = models.CharField(max_length=25)
    District = models.CharField(max_length=15)
    State = models.CharField(max_length=20)
    ContactNo = models.IntegerField()
    Paymentmethod = models.CharField(max_length=10)

class student(models.Model):
    name = models.CharField(max_length=10)
    cls = models.IntegerField()

class login(models.Model):
   username = models.CharField(max_length=30)
   password = models.CharField(max_length=10)