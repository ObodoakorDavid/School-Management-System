from django.urls import path
from . import views 

app_name = 'students'

urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('students/', views.students, name='index'),
    path('students/add/', views.add_student, name='addStudent'),
    path('students/detail/<id>', views.student_detail, name='student_detail' ),
    path('students/delete/<id>', views.student_delete, name='student_delete' ),
]