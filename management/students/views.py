from django.shortcuts import render
from . models import *
from . forms import *
from professors.models import EnrolledCourse, User, Student, Course, test
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import  render, redirect


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