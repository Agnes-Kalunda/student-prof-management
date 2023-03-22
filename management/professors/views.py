from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseNotFound
from django.db.models import Prefetch  
from django.views.generic import View

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
    publishedCourses = Course.objects.filter(professor=request.user.professor).all()

    course_data = []
    for course in publishedCourses:
        student_count = course.students.count()
        course_data.append({
            'course': course,
            'student_count': student_count,
        })
    return render(request, 'professors/professor.html', {'course_data': course_data, 'publishedCourses': publishedCourses})


def enrolled_students(request):
    publishedCourses = Course.objects.filter(professor=request.user.professor).all()
    course_data = []
    for course in publishedCourses:
        students = course.students.all()
        student_data = []
        for student in students:
            try:
                grade = Grade.objects.get(student=student, course=course)
                student_data.append({
                    'name': student.user.get_full_name(),
                    'grade': grade.grade,
                })
            except Grade.DoesNotExist:
                student_data.append({
                    'name': student.user.get_full_name(),
                    'grade': '-',
                })
        course_data.append({
            'course': course,
            'students': student_data,
        })
    return render(request, 'studentsEnrolled.html', {'course_data': course_data})

    

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
    
class EditCourseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['title', 'category', 'coursePoster', 'descriptions', 'body']
    template_name = 'professors/edit_course.html'

    def test_func(self):
        course = self.get_object()
        return course.professor == self.request.user.professor


class DeleteCourseView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'professors/delete_course.html'
    success_url = reverse_lazy('professor')

    def test_func(self):
        course = self.get_object()
        return course.professor == self.request.user.professor

class addTest(LoginRequiredMixin, CreateView):
    model = test
    fields = ['title','course', 'body']
    template_name = 'professors/newTest.html'
    def form_valid(self, form):
        # form.instance.professor=self.request.user
        return super().form_valid(form)
    
# View to display a list of all grades for a specific student
class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    fields = ['student', 'course', 'grade']
    template_name = 'createGrade.html'
    def form_valid(self, form):
        # form.instance.professor=self.request.user
        return super().form_valid(form)

class CourseDetailProf(LoginRequiredMixin, View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'professors/CourseDetailProf.html', {'course': course})
    
class TestDetailProf(LoginRequiredMixin, View):
    def get(self, request, pk):
        testProf =get_object_or_404(test, pk=pk)
        return render (request, 'TestProf.html', {'testProf':testProf})


class GradeListView(ListView):
    model = Grade
    template_name = 'grade_list.html'
    context_object_name = 'grades'

