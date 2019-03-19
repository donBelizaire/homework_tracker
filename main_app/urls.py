from django.urls import path, include
<<<<<<< HEAD
=======
from django.conf.urls import url
from . import views as views
>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
<<<<<<< HEAD
    # path('registration/signin/', views.signin, name='signin'),
    # path('registration', include('django.contrib.auth.urls')),
    # path('registration/signup/', views.signup, name='signup'),
=======
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c
]
