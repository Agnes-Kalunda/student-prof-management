from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from professors.views import ProfessorReg

urlpatterns = [
    
    path('prof/', views.professor, name='professor'),
    path('register-professor/', ProfessorReg.as_view(), name='professor-reg'),
    path('login-professor/', views.loginProfessor, name='professor-login'),
    path('logout-professor/', auth_views.LogoutView.as_view(), name='professor-logout'),
]