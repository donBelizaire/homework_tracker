"""homework_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
from django.conf.urls import url
>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c
from main_app import views as main_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', main_app_views.register, name='register'),
    path('', include('main_app.urls')),
    # url(r'^signup/$', main_app_views.signup, name='signup'),
]
