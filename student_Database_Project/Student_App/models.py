from django.db import models

# Create your models here.
from django.db import models

class Teacher(models.Model):
    DESIGNATIONS = [
        ('Teacher', 'Teacher'),
        ('Head of Department', 'Head of Department'),
        ('Principal', 'Principal'),
        ('Administrator', 'Administrator'),
    ]

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    school_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=30, choices=DESIGNATIONS)
    subjects = models.CharField(max_length=200)
    password = models.CharField(max_length=128)  # Store hashed password
    security_question = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"

from django.db import models

class Student(models.Model):
    YEARS = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    year = models.CharField(max_length=20, choices=YEARS)
    password = models.CharField(max_length=128)
    security_question = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"
