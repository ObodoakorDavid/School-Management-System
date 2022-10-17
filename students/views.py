from django.shortcuts import redirect, render
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
    return render(request, 'students/all_students.html', context)

@login_required(login_url='accounts:signup')
def add_student(request):
    print(request.user)
    form = StudentForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('students:index')
    return render(request, 'students/add_student.html', context)


def home_view(request):
    return render(request,'Home.html' )

def student_detail(request, id):
    student = Student.objects.get(pk=id)
    context = {
        'student': student
    }
    return render(request, 'students/student_detail.html', context)

def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('students:index')

def student_update(request, id):
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST or None, instance=student)
    context = {
        'form': form
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('students:index')
    return render(request, 'students/students_update.html', context)

