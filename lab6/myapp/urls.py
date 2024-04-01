from django.urls import path

from . import view

urlpatterns = [
    path('students/', view.students, name='students'),
    path('courses/', view.courses, name='courses'),
    path('students/<int:pk>/', view.student_details, name='student_details'),
]