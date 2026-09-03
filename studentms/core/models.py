from django.db import models


# ABSTRACT MODEL
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# MAIN STUDENT MODEL
class Student(BaseModel):
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
    profile_photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# PROFILE MODEL — with student one to one
class StudentProfile(BaseModel):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    guardian_name = models.CharField(max_length=200, blank=True, null=True)
    blood_group = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        choices=[
            ('A+', 'A+'), ('A-', 'A-'),
            ('B+', 'B+'), ('B-', 'B-'),
            ('O+', 'O+'), ('O-', 'O-'),
            ('AB+', 'AB+'), ('AB-', 'AB-'),
        ]
    )

    def __str__(self):
        return f"{self.student.full_name}'s Profile"