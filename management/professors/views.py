from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProfessorReg(CreateView):
    model = User
    form_class = ProfessorRegisterForm
    template_name = 'professors/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('professor-login')
    
def loginProfessor(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('professor')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'professors/login.html',
    context={'form':AuthenticationForm()})


def professor(request):

    publishedCourses = Course.objects.filter(professor = request.user.professor).all()
    # enroll = StudentProfile.enrolledIn
    # students = publishedCourses.students.all()

    students = Student.objects.filter(enrolls__id__in = publishedCourses).all()
    # instance = Student.objects.filter(enrolls__id__in = publishedCourses).values('user')[0]
    # print(students)
    count = students.count()
    print(count)
    return render(request, 'professors/professor.html', {'publishedCourses': publishedCourses, 'students': students, 'count': count})


def studentsEnrolled(request):
    publishedCourses = Course.objects.filter(professor = request.user.professor).all()
    # enroll = StudentProfile.enrolledIn
    # students = publishedCourses.students.all()

    students = Student.objects.filter(enrolls__id__in = publishedCourses).all()
    # instance = Student.objects.filter(enrolls__id__in = publishedCourses).values('user')[0]
    # print(students)
    count = students.count()
    print(count)
    
    return render(request, 'professors/studentsEnrolled.html',  {'publishedCourses': publishedCourses, 'students': students, 'count': count})

def publishedTests(request):
        publishedTests = test.objects.all()

        return render(request, 'professors/postedTest.html', {'publishedTests': publishedTests})


class addCourse(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title','category','coursePoster', 'descriptions', 'body']
    template_name = 'professors/newCourse.html'
    def form_valid(self, form):
        form.instance.professor=self.request.user.professor
        return super().form_valid(form)

class addTest(LoginRequiredMixin, CreateView):
    model = test
    fields = ['title','course', 'body']
    template_name = 'professors/newTest.html'
    def form_valid(self, form):
        # form.instance.professor=self.request.user
        return super().form_valid(form)