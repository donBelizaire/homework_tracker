from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'users/index.html')

def signin(request):
    return render(request, 'registration/signin.html')

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials = try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=256, required=True)
    location = forms.CharField(max_length=30, required=True)
    class_start_date = forms.CharField(max_length=30, required=True)
    class_type = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'location', 'class_start_date', 'class_type', 'password1', 'password2'}
