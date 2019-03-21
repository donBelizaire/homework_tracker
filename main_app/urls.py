from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('student_detail/', views.student_detail, name="student_detail"),
    path('instructor/cohort_select/', views.cohort_select, name="cohort_select"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/create_profile/', views.create_profile, name='create_profile'),
    # path('accounts/register/<int:user_id>', views.registration, name='registration'),
]
