from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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


# def professor(request):

#     publishedCourses = Course.objects.filter(professor = request.user.professor).first()
#     # enroll = StudentProfile.enrolledIn
#     # students = publishedCourses.students.all()

#     if not publishedCourses:
#          return HttpResponseNotFound()
    
#     enrolled_students= publishedCourses.students.all()

#     count = enrolled_students.count()
         
    # students = Student.objects.filter(enrolls__id__in = publishedCourses).all()
    # count = students.count()





    # course_counts = {}
    # for course in publishedCourses:
    #     enrolled_students = course.students.all()
    #     course_counts[course.title] = enrolled_students.count()

    # count = students.count()
    # print(course_counts)
    # return render(request, 'professors/professor.html', {'publishedCourses': publishedCourses,  'count': count})



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
    # return render(request, 'professors/professor.html', {'course_data': course_data, 'publishedCourses': publishedCourses})

    # instance = Student.objects.filter(enrolls__id__in = publishedCourses).values('user')[0]
    # print(students)
    # count = students.count()
    # print(count)
    # return render(request, 'professors/professor.html', {'publishedCourses': publishedCourses, 'students': students, 'count': count})


def enrolled_students(request):

    publishedCourses = Course.objects.filter(professor = request.user.professor).all()
    # enroll = StudentProfile.enrolledIn
    # students = publishedCourses.students.all()

    students = Student.objects.filter(enrolls__id__in = publishedCourses).all()
    # instance = Student.objects.filter(enrolls__id__in = publishedCourses).values('user')[0]
    print(students)
    # count = students.count()
    # print(count)
    return render(request, 'studentsEnrolled.html', {'publishedCourses': publishedCourses, 'students': students})
    
    # students = Student.objects.filter(enrolls__id__in = publishedCourses).all()
    # instance = Student.objects.filter(enrolls__id__in = publishedCourses).values('user')[0]
    # print(students)
    # count = students.count()
    # print(count)
    
    # return render(request, 'professors/studentsEnrolled.html',  {'publishedCourses': publishedCourses, 'students': students, 'count': count})

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
    
# View to display a list of all grades for a specific student
class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    fields = ['student', 'course', 'grade']
    template_name = 'createGrade.html'
    def form_valid(self, form):
        # form.instance.professor=self.request.user
        return super().form_valid(form)

# class CourseDetail(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         displayedCourses =get_object_or_404(Course, pk=pk)
#         return render (request, 'professors/course.html', {'displayedCourses':displayedCourses})
    

    # return render(request, 'professors/course
# class GradeUpdateView(LoginRequiredMixin, UpdateView):
#     model = Grade
#     fields = ['student', 'course', 'grade']
#     template_name = 'updateGrade.html'
#     def form_valid(self, form):
#         # form.instance.professor=self.request.user
#         return super().form_valid(form)

# class GradeDeleteView(LoginRequiredMixin, DeleteView):
#     model = Grade
#     success_url = reverse_lazy('grades_list')
#     template_name = 'grades/delete.html'