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
    ContactNo = models.CharField(max_length=10)
    Paymentmethod = models.CharField(max_length=10)

class student(models.Model):
    name = models.CharField(max_length=10)
    cls = models.IntegerField()

class login(models.Model):
   username = models.CharField(max_length=30)
   password = models.CharField(max_length=10)

class hospitalreg(models.Model):
    Hid=models.IntegerField(primary_key=True)
    Hname=models.CharField(max_length=30)
    Place=models.CharField(max_length=25)
    Address=models.CharField(max_length=50)
    email=models.EmailField()
    Contact=models.CharField(max_length=10)

class doctorreg(models.Model):
    Did=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=20)
    Hid=models.IntegerField()
    Department=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=10)
    Time=models.DateTimeField()

