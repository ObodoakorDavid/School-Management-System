from django.db import models
import uuid

# Create your models here.

class Student(models.Model):
    student_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.ForeignKey('Course', on_delete=models.CASCADE)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

class Course(models.Model):
    course_choices = models.CharField(max_length=50)

    def __str__(self):
        return self.course_choices
