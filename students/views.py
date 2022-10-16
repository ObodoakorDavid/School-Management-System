from multiprocessing import context
from django.shortcuts import render
from .models import Student
from .form import StudentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts:signup')
def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/allStudents.html', context)

@login_required(login_url='accounts:signup')
def add_student(request):
    print(request.user)
    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'students/addStudent.html', context)


def home_view(request):
    return render(request,'Home.html' )
