# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class Exclusion(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    reason = models.TextField()

class BusMileage(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE)
    initial_mileage = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed


class Parent(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Operator(models.Model):
    name = models.CharField(max_length=100)
    
    # Add other fields as needed

class Bus(models.Model):
    number = models.CharField(max_length=20)
    # Add other fields as needed

class BusTrack(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # Add other fields as needed

class Feedback(models.Model):
    message = models.TextField()
    # Add other fields as needed
    
class PopRegister(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    operator = models.ForeignKey('Operator', on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    timestamp = models.DateTimeField(auto_now_add=True)


class Child(models.Model):
    name = models.CharField(max_length=100)
    ucs_number = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)

class BusStop(models.Model):
    bus_stage_name = models.CharField(max_length=100)
    pick_drop_time = models.TimeField()


class User(AbstractUser):
    # Your custom user model fields, if needed
    pass

