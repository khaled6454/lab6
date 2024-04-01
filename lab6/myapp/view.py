from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students, 'form': form})

def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def student_details(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students.html', {'student': student})