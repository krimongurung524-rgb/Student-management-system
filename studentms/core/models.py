from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    GRADE_CHOICES = [
        ('grade_9', 'Grade 9'),
        ('grade_10', 'Grade 10'),
        ('grade_11', 'Grade 11'),
        ('grade_12', 'Grade 12'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    address = models.TextField()
    slug = models.SlugField(unique=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name