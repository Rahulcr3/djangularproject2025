from django.db import models

# Create your models here.
from django. contrib. auth.models import AbstractUser

class User(AbstractUser):
    usertype=models.CharField(max_length=50)

class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone_no=models.IntegerField()
    salary=models.IntegerField()
    experience=models.IntegerField()

class Student(models.Model):
    student_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    guardian=models.CharField(max_length=255)




