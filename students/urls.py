from django.urls import URLPattern, path
from . import views 

app_name = 'students'

urlpatterns = [
    path('students', views.students, name='index'),
    path('students/add/', views.add_student, name='addStudent'),
    path('', views.home_view, name='homepage')
]