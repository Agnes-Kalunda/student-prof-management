from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from professors.views import ProfessorReg

urlpatterns = [
    path('register-professor/', ProfessorReg.as_view(), name='professor-reg'),
]