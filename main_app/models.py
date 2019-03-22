from django import forms
from django.db import models
from django.urls import reverse
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200,choices=USERTYPE_CHOICES)
    location = models.CharField(max_length=200,choices=LOCATION_CHOICES)
    class_start_date = models.CharField(max_length=200,choices=DATE_CHOICES, default='Jan-2019')
    class_type = models.CharField(max_length=200, choices=CLASSTYPE_CHOICES)

    def __str__(self):
        return f'{self.user} Profile'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

#     def __str__(self):
#         return self.name

# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# class Cohort(models.Model):
#         user = models.OneToOneField(User, on_delete=models.CASCADE)

# class AssignmentUpload(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# UNCOMMENT THIS LATER

# class SignUpForm(models.Model):
#     first_name = models.CharField(max_length=30, label='First Name', help_text='First Name')
#     last_name = models.CharField(max_length=30, label='Last Name', help_text='Last Name') 
#     username = models.CharField(max_length=30, label='Username', help_text='Username')
#     email = models.EmailField(max_length=250, label='Email', help_text='Email')
#     location = models.CharField(max_length=30, label='Location', help_text='Location')
#     class_start_date = models.CharField(max_length=30, label='Start Date', help_text='Start Date')
#     class_type = models.CharField(max_length=30, label='Class Type', help_text='Class Type')  

# class CohortCreate(models.Model):
#     city = models.CharField(max_length=30, label='City')
#     start_date = models.DateField(max_length=30, label='Start Date')
#     class_type = models.CharField(max_length=30, label='Class Type')
