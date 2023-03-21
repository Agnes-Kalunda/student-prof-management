from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from professors.views import ProfessorReg, addCourse, addTest, GradeCreateView, CourseDetailProf, TestDetailProf, EditCourseView, DeleteCourseView

urlpatterns = [
    path('prof/', views.professor, name='professor'),
    path('register-professor/', ProfessorReg.as_view(), name='professor-reg'),
    path('login-professor/', views.loginProfessor, name='professor-login'),
    path('logout-professor/', auth_views.LogoutView.as_view(), name='professor-logout'),
    path('new-course/', addCourse.as_view(), name='new-course'),
    path('edit_course/<int:pk>/', EditCourseView.as_view(), name='edit_course'),
    path('delete_course/<int:pk>/', DeleteCourseView.as_view(), name='delete_course'),
    path('new-test/', addTest.as_view(), name='new-test'),
    path('posted-tests/', views.publishedTests, name='postedTest'),
    path('studentsEnrolled/', views.enrolled_students, name='studentsEnrolled'),
    path('create_grade/', GradeCreateView.as_view(), name='create_grade'),
    path('CourseDetailProf/<int:pk>/', CourseDetailProf.as_view(), name='CourseDetailProf'),
    path('TestDetailProf/<int:pk>/', TestDetailProf.as_view(), name='TestDetailProf'),
]
