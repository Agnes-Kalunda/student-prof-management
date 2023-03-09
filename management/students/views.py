from django.shortcuts import render

from professors.models import EnrolledCourse, User, Student, Course, test

# Create your views here.


def students(request):
    courses = Course.objects.all()
    tests = test.objects.all()
    currentUser = request.user.student
    # activeCourses = get_object_or_404(Course, studentprofile=currentUser.pk)
    activeCourses = Course.objects.filter(students=currentUser.pk).all()


    return render(request, 'students/dashboard.html', {'courses': courses, 'tests': tests, 'activeCourses':activeCourses})

