<<<<<<< HEAD
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
=======
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login 
>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'users/index.html')

def signin(request):
    return render(request, 'registration/signin.html')

<<<<<<< HEAD
# def signup(request):
    # error_message=''
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         login(request, user)
    #         return redirect('index')
    #     else:
    #         error_message = 'Invalid credentials = try again'
    # form = UserCreationForm()
    # context = {'form': form, 'error_message': error_message}
    # return render(request, 'registration/signup.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
=======
def signup(request):
  error_message=''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials - try again'
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)
#     email = forms.EmailField(max_length=256, required=True)
#     location = forms.CharField(max_length=30, required=True)
#     class_start_date = forms.CharField(max_length=30, required=True)
#     class_type = forms.CharField(max_length=30, required=True)

#     class Meta:
#         model = User
#         fields = {'first_name', 'last_name', 'email', 'location', 'class_start_date', 'class_type', 'password1', 'password2'}
>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c
