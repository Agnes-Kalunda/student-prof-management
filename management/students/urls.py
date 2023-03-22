from django.urls import path
from django.contrib.auth import views as auth_views
from . import  views
from students.views import studentReg, courseEnroll, markComplete, CourseDetail, TestDetail



urlpatterns = [
    path ('dashboard/', views.students, name='students'),
    path('register/', studentReg.as_view(), name='register'),
    path('login/', views.loginStudent, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('enroll/<int:pk>/',courseEnroll.as_view(), name='enroll'),
    path('complete/<int:pk>/', markComplete.as_view(), name='complete'),
    path('programs/', views.availablePrograms, name='programs'),


    
    path('course-detail/<int:pk>/', CourseDetail.as_view(), name='courseDetail'),
   
    
    path('test-detail/<int:pk>/', TestDetail.as_view(), name='testDetail'),
    # path('student/', CourseView.as_view(), name='student'),

]