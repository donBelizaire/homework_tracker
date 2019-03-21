from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class SignUpForm(models.Model):
    first_name = models.CharField(max_length=30, label='First Name', help_text='First Name')
    last_name = models.CharField(max_length=30, label='Last Name', help_text='Last Name') 
    username = models.CharField(max_length=30, label='Username', help_text='Username')
    email = models.EmailField(max_length=250, label='Email', help_text='Email')
    location = models.CharField(max_length=30, label='Location', help_text='Location')
    class_start_date = models.CharField(max_length=30, label='Start Date', help_text='Start Date')
    class_type = models.CharField(max_length=30, label='Class Type', help_text='Class Type')  

class CohortCreate(models.Model):
    city = models.CharField(max_length=30, label='City')
    start_date = models.DateField(max_length=30, label='Start Date')
    class_type = models.CharField(max_length=30, label='Class Type')