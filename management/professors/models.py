from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    is_professor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()


#studentModel
class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='student',primary_key = True) 
    # courseInterest = models.TextField()

    def __str__(self):
        return self.user.first_name

#professorModel 
class Professor(models.Model):
    user = models.OneToOneField(User, related_name='professor', on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
            return self.user.first_name
    


#courseModel
class Course(models.Model):
    professor=models.ForeignKey(Professor, on_delete=models.CASCADE)
    title=models.CharField(max_length=100) 
    descriptions=models.CharField(max_length=100) 
    body = models.TextField()
    coursePoster = models.ImageField(upload_to='coursePoster')
    category = models.CharField(max_length=100)
    students= models.ManyToManyField(Student, related_name='enrolls' )
    # students = models.ForeignKey(Student, related_name='enrolls', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('professor')