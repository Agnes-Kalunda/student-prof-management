from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from professors.views import ProfessorReg, addCourse, addTest

urlpatterns = [
    
    path('prof/', views.professor, name='professor'),
    path('register-professor/', ProfessorReg.as_view(), name='professor-reg'),
    path('login-professor/', views.loginProfessor, name='professor-login'),
    path('logout-professor/', auth_views.LogoutView.as_view(), name='professor-logout'),
    path('new-course/', addCourse.as_view(), name='new-course'),
    path('new-test/', addTest.as_view(), name='new-test'),
    path('posted-tests/', views.publishedTests, name = 'postedTest'), #postedTests
]