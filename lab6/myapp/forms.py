from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'enrollment_year', 'courses']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code']

class EnrollCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        student_id = kwargs.pop('student_id', None)
        super().__init__(*args, **kwargs)
        if student_id:
            enrolled_courses = Student.objects.get(id=student_id).courses.all()
            self.fields['course'].queryset = Course.objects.exclude(id__in=enrolled_courses)