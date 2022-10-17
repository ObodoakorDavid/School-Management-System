from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    gpa = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

class Course(models.Model):
    course_choices = models.CharField(max_length=50)

    def __str__(self):
        return self.course_choices
