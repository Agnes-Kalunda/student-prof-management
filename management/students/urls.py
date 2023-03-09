from django.urls import path
from django.contrib.auth import views as auth_views
from . import  views
from students.views import studentReg


urlpatterns = [
    path ('dashboard/', views.students, name='students'),
    path('register/', studentReg.as_view(), name='register'),
    path('login/', views.loginStudent, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]