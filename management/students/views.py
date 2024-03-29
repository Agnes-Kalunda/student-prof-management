from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from professors.models import Grade, EnrolledCourse, Course
from . models import * 
from django.urls import reverse_lazy
from . forms import *


from professors.models import EnrolledCourse, User, Student, Course, test
# Create your views here.


def students(request):
    courses = Course.objects.all()
    tests = test.objects.all()
    currentUser = request.user.student
    # activeCourses = get_object_or_404(Course, studentprofile=currentUser.pk)
    activeCourses = Course.objects.filter(students=currentUser.pk).all()


    return render(request, 'students/dashboard.html', {'courses': courses, 'tests': tests, 'activeCourses':activeCourses})


class studentReg(CreateView):
    model = User
    form_class = StudentRegisterForm
    template_name = 'students/register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
    
def loginStudent(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('students')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'students/login.html',
    context={'form':AuthenticationForm()})

class courseEnroll(LoginRequiredMixin, View):
     def post(self, request, pk, *args, **kwargs):
        course = Course.objects.get(pk=pk)
        course.students.add(request.user.student)
        return redirect('programs')


class markComplete(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        course = Course.objects.get(pk=pk)
        is_student = False


        for student in course.students.all():
            if student == request.user.student:
                is_student = True
                break

        if not is_student:
            course.students.remove(request.user.student)

def availablePrograms(request): 
    courses = Course.objects.all()
    return render(request, 'students/availablePrograms.html', {'courses': courses})



class CourseDetail(LoginRequiredMixin, View):
    template_name = 'professors/course.html'

    def get(self, request, pk, *args, **kwargs):
        # Get the current student
        student = request.user.student
        
        # Retrieve the course instance
        displayed_course = get_object_or_404(Course, pk=pk)
        
        try:
            # Retrieve the grade instance for the current student and course
            grade = Grade.objects.get(student=student, course=displayed_course)
        except Grade.DoesNotExist:
            # If no grade instance is found, set the grade to None
            grade = None

        # Render the student template with the course and grade instances
        context = {
            'displayed_course': displayed_course,
            'grade': grade,
        }
        return render(request, self.template_name, context)


class TestDetail(LoginRequiredMixin, View):
    def get(self, request, pk):
        displayedtest =get_object_or_404(test, pk=pk)
        return render (request, 'professors/test.html', {'displayedtest':displayedtest})




# class CourseView(View):
#     template_name = 'professors/course.html'

#     def get(self, request, *args, **kwargs):
#         # Get the current student
#         student = request.user.student
        
#         # Retrieve the grade instance from the professor's model
#         grade = Grade.objects.filter(student=student).first()

#         # Render the student template with the grade instance
#         context = {
#             'grade': grade,
#         }
#         return render(request, self.template_name, context)