<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django import forms

# class CustomUser(AbstractUser):
#     is_instructor = models.BooleanField(default=False)
#     first_name = forms.CharField(max_length=30, required=True, label = "First Name")
#     last_name = forms.CharField(max_length=30, required=True, label = "Last Name")
#     email = forms.EmailField(max_length=256, required=True, label = "E-mail")
#     location = forms.CharField(max_length=30, required=True, label = "Location")
#     class_start_date = forms.CharField(max_length=30, required=True, label = "Start Date")
#     class_type = forms.CharField(max_length=30, required=True, label = "Class Type")
#     def __str__(self):
#         return self.email
=======
from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c
