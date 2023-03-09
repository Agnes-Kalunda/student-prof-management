from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
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
    

